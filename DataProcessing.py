import pandas as pd
from config import FILTER_CONDITIONS
class DataProcessing:
    # ==========================================
    # 1. Load data
    # ==========================================
    @staticmethod
    def load_data(file_path):
        df = pd.read_csv(file_path)
        print("=== First 5 Rows ===")
        print(df.head())
        print("\n=== Data Information ===")
        print(df.info())
        print("\n=== Descriptive Statistics ===")
        print(df.describe())
        return df

    # ==========================================
    # 2. Data cleaning & filtering
    # ==========================================
    @staticmethod
    def clean_data(df):
        df_clean = df.dropna()
        df_filtered = df_clean[(df_clean["AGE"] > FILTER_CONDITIONS["min_age"]) & (df_clean["LIMIT_BAL"] > FILTER_CONDITIONS["min_limit"])]
        return df_filtered

    # ==========================================
    # 3. Core analysis
    # ==========================================
    @staticmethod
    def analyze_default_rate(df):
        # Analyze by age
        age_default = df.groupby("AGE")["default"].mean()
        
        # Analyze by credit limit
        limit_default = df.groupby("LIMIT_BAL")["default"].mean()
        
        return {
        "age_default_rate": age_default,
        "limit_default_rate": limit_default,
    }
