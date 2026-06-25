import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import mean_absolute_error
import xgboost as xgb

from src.data.cleaner import load_and_clean
from src.features.engineer import encode_features
from config import paths, config


def naive_baseline_mae(df_test: pd.DataFrame) -> float:
    """Baseline: predict 2025 score = 2024 score. Our model must beat this."""
    return mean_absolute_error(df_test["score_min"], df_test["score_prev_year"])


def train():
    df = load_and_clean()

    # Temporal split — train on 2024, validate on 2025
    df_train = df[df["year"] == 2024].copy()
    df_test  = df[df["year"] == 2025].copy()

    print(f"Train : {len(df_train)} rows (2024)")
    print(f"Test  : {len(df_test)} rows (2025)")

    # Naive baseline
    baseline_mae = naive_baseline_mae(df_test)
    print(f"\nNaive baseline MAE : {baseline_mae:.3f} pts")
    print("(predicting: 2025 score = 2024 score)")
    print("Our model must beat this.\n")

    # Encode
    X_train, y_train, encoders = encode_features(df_train, fit=True)
    X_test,  y_test,  _        = encode_features(df_test,  fit=False, encoders=encoders)

    # Train XGBoost
    model = xgb.XGBRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=4,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        verbosity=0
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred   = model.predict(X_test)
    test_mae = mean_absolute_error(y_test, y_pred)

    print(f"XGBoost MAE on 2025 : {test_mae:.3f} pts")
    print(f"Baseline MAE        : {baseline_mae:.3f} pts")
    print(f"Improvement         : {baseline_mae - test_mae:+.3f} pts")

    if test_mae >= baseline_mae:
        print("\nWARNING: model does not beat naive baseline.")
        print("score_prev_year alone is the strongest signal we have.")
    else:
        print("\nModel beats naive baseline.")

    # Feature importance
    print("\nFeature importance:")
    for feat, imp in sorted(
        zip(config.feature_cols, model.feature_importances_),
        key=lambda x: -x[1]
    ):
        bar = "█" * int(imp * 40)
        print(f"  {feat:20s}: {imp:.3f}  {bar}")

    # Test with your sister (Bac Math)
    print("\n--- Test: your sister (Bac Mathematiques) ---")
    math_2025 = df_test[df_test["bac_type"] == "Mathematiques"].copy()
    math_pred = model.predict(
        encode_features(math_2025, fit=False, encoders=encoders)[0]
    )
    math_mae = mean_absolute_error(math_2025["score_min"], math_pred)
    print(f"MAE for Mathematiques only: {math_mae:.3f} pts")
    print(f"Sample predictions vs actual:")
    math_2025["predicted"] = math_pred.round(2)
    print(
        math_2025[["filiere_name", "université", "score_min", "predicted"]]
        .head(5)
        .to_string(index=False)
    )

    # Save bundle
    bundle = {
        "model":        model,
        "encoders":     encoders,
        "feature_cols": config.feature_cols,
        "test_mae":     test_mae,
        "baseline_mae": baseline_mae,
        "train_year":   2024,
        "test_year":    2025,
        "predict_year": 2026,
    }

    paths.models_dir.mkdir(exist_ok=True)
    with open(paths.model_bundle, "wb") as f:
        pickle.dump(bundle, f)

    print(f"\nSaved → {paths.model_bundle}")
    return bundle


if __name__ == "__main__":
    train()