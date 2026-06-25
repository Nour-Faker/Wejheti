import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException
from config import paths, app_config
from src.api.schemas import StudentProfile, ProgramResult, OrientationResponse
from src.features.engineer import encode_features
from src.data.cleaner import load_and_clean
# Load model bundle once at startup
with open(paths.model_bundle, "rb") as f:
    bundle = pickle.load(f)

model    = bundle["model"]
encoders = bundle["encoders"]

# Load full data for filiere lookup
df_full = load_and_clean()
df_2025 = df_full[df_full["year"] == 2025].copy()
# Build filiere name lookup from ALL years (more coverage)
name_lookup = (
    df_full[["code_filiere", "filiere_name"]]
    .dropna()
    .drop_duplicates("code_filiere")
    .set_index("code_filiere")["filiere_name"]
    .to_dict()
)
app = FastAPI(
    title=app_config.name,
    description=app_config.description,
    version=app_config.version
)


def classify_chance(student_score: float, predicted_score: float) -> tuple[str, str]:
    gap = student_score - predicted_score
    if gap >= 5:
        return "safe",  "✅ Accessible"
    elif gap >= -3:
        return "match", "🎯 Dans tes cordes"
    else:
        return "reach", "🚀 Ambitieux"


@app.get("/", tags=["Health"])
def root():
    return {
        "app":     app_config.name,
        "version": app_config.version,
        "status":  "running"
    }


@app.get("/bac_types", tags=["Data"])
def get_bac_types():
    return {"bac_types": sorted(df_2025["bac_type"].unique().tolist())}


@app.get("/universities", tags=["Data"])
def get_universities():
    return {"universities": sorted(df_2025["université"].unique().tolist())}


@app.post("/orientation", response_model=OrientationResponse, tags=["Wejheti"])
def get_orientation(profile: StudentProfile):
    """
    Core endpoint — given bac type and score,
    returns safe / match / reach university programs.
    """
    # Filter 2025 data for this bac type
    df_bac = df_2025[df_2025["bac_type"] == profile.bac_type].copy()

    if df_bac.empty:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for bac type: {profile.bac_type}"
        )

    # Predict 2026 scores for all programs
    X, _, _ = encode_features(df_bac, fit=False, encoders=encoders)
    df_bac["predicted_2026"] = model.predict(X).round(4)

    # Classify each program
    results = {"safe": [], "match": [], "reach": []}

    for _, row in df_bac.iterrows():
        chance, label = classify_chance(profile.score, row["predicted_2026"])
        delta = round(row["predicted_2026"] - row["score_min"], 4)
        trend = "↑" if delta > 1 else ("↓" if delta < -1 else "→")

        program = ProgramResult(
            filiere_name=row["filiere_name"],
            universite=row["université"],
            code_filiere=str(row["code_filiere"]),
            predicted_score_2026=row["predicted_2026"],
            score_2025=row["score_min"],
            delta=delta,
            trend=trend,
            chance=chance,
            chance_label=label
        )
        results[chance].append(program)

    # Sort each category by predicted score descending
    for key in results:
        results[key].sort(key=lambda x: x.predicted_score_2026, reverse=True)

    return OrientationResponse(
        student_score=profile.score,
        bac_type=profile.bac_type,
        safe=results["safe"],
        match=results["match"],
        reach=results["reach"],
        total_programs=len(df_bac)
    )
