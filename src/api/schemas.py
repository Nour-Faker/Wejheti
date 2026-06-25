from pydantic import BaseModel, field_validator
from typing import List


class StudentProfile(BaseModel):
    bac_type: str
    score: float

    @field_validator("bac_type")
    @classmethod
    def validate_bac(cls, v):
        valid = [
            "Mathematiques", "Sciences", "Technique",
            "Informatique", "Economie", "Lettres", "Sport"
        ]
        if v not in valid:
            raise ValueError(f"bac_type must be one of {valid}")
        return v

    @field_validator("score")
    @classmethod
    def validate_score(cls, v):
        if not (60 <= v <= 220):
            raise ValueError("score must be between 60 and 220")
        return v


class ProgramResult(BaseModel):
    filiere_name: str
    universite: str
    code_filiere: str
    predicted_score_2026: float
    score_2025: float
    delta: float
    trend: str
    chance: str        # "safe" | "match" | "reach"
    chance_label: str  # "✅ Accessible" | "🎯 Dans tes cordes" | "🚀 Ambitieux"


class OrientationResponse(BaseModel):
    student_score: float
    bac_type: str
    safe:  List[ProgramResult]
    match: List[ProgramResult]
    reach: List[ProgramResult]
    total_programs: int