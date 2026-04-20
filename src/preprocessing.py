import pandas as pd
import numpy as np

def clean_phishing(input_path, output_path):
    df = pd.read_csv(input_path)

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)

    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_phishing(
        "data/raw/phishing.csv",
        "data/processed/phishing_clean.csv"
    )
