from pathlib import Path

BASE_DIR = Path(__file__).parent

class Paths:
    clean_data   = BASE_DIR / "data" / "clean_scores.csv"
    full_data    = BASE_DIR / "data" / "full_clean_scores.csv"
    models_dir   = BASE_DIR / "models"
    model_bundle = BASE_DIR / "models" / "bundle_v1.pkl"
    outputs_dir  = BASE_DIR / "outputs"
    predictions  = BASE_DIR / "outputs" / "predictions_2026.csv"

class ModelConfig:
    target_col   = "score_min"
    feature_cols = [
        "univ_enc",
        "filiere_enc",
        "bac_enc",
        "score_prev_year",
        "score_delta"
    ]
    predict_year = 2026

class AppConfig:
    name        = "Wejheti — وجهتي"
    version     = "1.0.0"
    description = "Aide les étudiants tunisiens à choisir leur orientation universitaire"
    host        = "0.0.0.0"
    port        = 8000

paths  = Paths()
config = ModelConfig()
app_config = AppConfig()