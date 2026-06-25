import pandas as pd
from config import paths


def load_and_clean() -> pd.DataFrame:
    df = pd.read_csv(paths.clean_data)

    # Drop PDF artifact
    if "page" in df.columns:
        df = df.drop(columns=["page"])

    # Drop rows missing critical values
    df = df.dropna(subset=["score_min", "score_prev_year"])

    # Compute score_delta: how much did this filière change?
    df = df.sort_values(["code_filiere", "bac_type", "year"])
    df["score_delta"] = df["score_min"] - df["score_prev_year"]

    # Clean types
    df["year"]         = df["year"].astype(int)
    df["score_min"]    = df["score_min"].astype(float)
    df["code_filiere"] = df["code_filiere"].astype(str)

    return df.reset_index(drop=True)


if __name__ == "__main__":
    df = load_and_clean()
    print(f"Shape        : {df.shape}")
    print(f"Columns      : {df.columns.tolist()}")
    print(f"Years        : {sorted(df['year'].unique())}")
    print(f"Bac types    : {sorted(df['bac_type'].unique())}")
    print(f"Filieres     : {df['code_filiere'].nunique()}")
    print(f"Nulls        : {df.isnull().sum().sum()}")
    print()
    print(df.head(3).to_string())