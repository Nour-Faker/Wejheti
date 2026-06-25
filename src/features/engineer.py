import pandas as pd
from sklearn.preprocessing import LabelEncoder
from config import config


def encode_features(df: pd.DataFrame, fit: bool = True, encoders: dict = None):
    """
    fit=True  → fit new encoders (used during training)
    fit=False → use existing encoders (used during inference)
    """
    df = df.copy()

    if fit:
        encoders = {
            "le_univ":    LabelEncoder(),
            "le_filiere": LabelEncoder(),
            "le_bac":     LabelEncoder(),
        }
        df["univ_enc"]    = encoders["le_univ"].fit_transform(df["université"])
        df["filiere_enc"] = encoders["le_filiere"].fit_transform(df["code_filiere"])
        df["bac_enc"]     = encoders["le_bac"].fit_transform(df["bac_type"])

    else:
        # Inference — handle unseen labels gracefully
        for col, enc_key, new_col in [
            ("université",   "le_univ",    "univ_enc"),
            ("code_filiere", "le_filiere", "filiere_enc"),
            ("bac_type",     "le_bac",     "bac_enc"),
        ]:
            known = set(encoders[enc_key].classes_)
            df[col] = df[col].apply(
                lambda x: x if x in known else encoders[enc_key].classes_[0]
            )
            df[new_col] = encoders[enc_key].transform(df[col])

    X = df[config.feature_cols]
    y = df[config.target_col] if config.target_col in df.columns else None

    return X, y, encoders


if __name__ == "__main__":
    from src.data.cleaner import load_and_clean

    df = load_and_clean()

    # Test on 2024 data
    df_train = df[df["year"] == 2024].copy()
    X, y, encoders = encode_features(df_train, fit=True)

    print(f"X shape  : {X.shape}")
    print(f"Columns  : {X.columns.tolist()}")
    print(f"Encoders : {list(encoders.keys())}")
    print()
    print(X.head(3).to_string())