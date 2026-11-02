"""
Data Loader Module for Student Performance Prediction
Demonstrates File Handling, Exception Handling, OOP, and Pandas operations.
"""

import os
import pandas as pd

class DataLoader:
    """Class responsible for safely loading and inspecting student dataset files."""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None

    def load_data(self) -> pd.DataFrame:
        """Loads dataset from CSV file using robust exception handling."""
        try:
            if not os.path.exists(self.filepath):
                print(f"[INFO] Dataset not found at '{self.filepath}'. Fetching directly from Kaggle Hub via kagglehub...")
                from dataset.download_kaggle_dataset import fetch_and_prepare_kaggle_dataset
                fetch_and_prepare_kaggle_dataset(os.path.dirname(self.filepath) or "dataset")
            
            print(f"[INFO] Reading dataset from: {self.filepath}")
            self.df = pd.read_csv(self.filepath)
            
            if self.df.empty:
                raise pd.errors.EmptyDataError("The dataset file is empty.")
                
            print(f"[SUCCESS] Successfully loaded {len(self.df)} student records with {len(self.df.columns)} columns.")
            return self.df
            
        except FileNotFoundError as fnf_err:
            print(f"[ERROR] File Error: {fnf_err}")
            raise
        except pd.errors.EmptyDataError as empty_err:
            print(f"[ERROR] Empty Data Error: {empty_err}")
            raise
        except Exception as e:
            print(f"[ERROR] An unexpected error occurred while loading data: {e}")
            raise

    def get_summary(self) -> dict:
        """Returns summary statistics and missing value counts using Python dictionary."""
        if self.df is None:
            raise ValueError("Data not loaded yet. Call load_data() first.")
            
        summary = {
            "total_records": len(self.df),
            "columns": list(self.df.columns),
            "missing_values": self.df.isnull().sum().to_dict(),
            "numerical_summary": self.df.describe().to_dict()
        }
        return summary

if __name__ == "__main__":
    # Test Data Loader standalone
    loader = DataLoader("../dataset/student_data.csv")
    df = loader.load_data()
    print("Columns:", loader.get_summary()["columns"])
