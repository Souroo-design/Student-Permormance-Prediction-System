"""
Data Preprocessing Module for Student Performance Prediction
Includes data cleaning, missing value handling, categorical encoding,
feature scaling, train-test splitting, and custom sorting implementations.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    """Class to clean, encode, and scale student academic data."""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.feature_columns = None
        self.is_fitted = False

    def clean_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handles missing values in numerical columns using median imputation."""
        df_clean = df.copy()
        
        # Identify missing values
        null_counts = df_clean.isnull().sum()
        for col in df_clean.columns:
            if null_counts[col] > 0:
                if df_clean[col].dtype in ['float64', 'int64']:
                    median_val = df_clean[col].median()
                    df_clean[col] = df_clean[col].fillna(median_val)
                    print(f"[PREPROCESSING] Imputed {null_counts[col]} missing values in '{col}' with median: {median_val:.2f}")
                else:
                    mode_val = df_clean[col].mode()[0]
                    df_clean[col] = df_clean[col].fillna(mode_val)
                    print(f"[PREPROCESSING] Imputed {null_counts[col]} missing values in '{col}' with mode: {mode_val}")
        return df_clean

    def encode_categorical(self, df: pd.DataFrame) -> pd.DataFrame:
        """Encodes categorical variables into numerical values."""
        df_encoded = df.copy()
        
        # Binary encoding
        if 'Internet_Access' in df_encoded.columns:
            df_encoded['Internet_Access'] = df_encoded['Internet_Access'].map({'Yes': 1, 'No': 0})
            
        return df_encoded

    def prepare_features_and_targets(self, df: pd.DataFrame):
        """Extracts X (feature matrix) and y (regression & classification targets)."""
        df_clean = self.clean_missing_values(df)
        df_encoded = self.encode_categorical(df_clean)
        
        # Define feature columns
        self.feature_columns = [
            'Attendance_Percentage',
            'Study_Hours_Per_Week',
            'Previous_Marks',
            'Assignment_Score',
            'Class_Participation',
            'Internet_Access'
        ]
        
        X = df_encoded[self.feature_columns]
        y_reg = df_encoded['Final_Score']
        y_clf = df_encoded['Pass_Fail'].map({'Pass': 1, 'Fail': 0})
        
        return X, y_reg, y_clf

    def fit_transform_scaling(self, X_train: pd.DataFrame) -> np.ndarray:
        """Fits StandardScaler on training data and returns scaled array."""
        X_scaled = self.scaler.fit_transform(X_train)
        self.is_fitted = True
        return X_scaled

    def transform_scaling(self, X: pd.DataFrame) -> np.ndarray:
        """Transforms input data using fitted StandardScaler."""
        if not self.is_fitted:
            raise ValueError("Scaler has not been fitted yet!")
        return self.scaler.transform(X)


# Custom sorting algorithm requirement from syllabus (Sorting demonstration)
def custom_bubble_sort_students(student_records: list, key_index: int = 1, reverse: bool = True) -> list:
    """
    Syllabus Topic: Manual Sorting Algorithm (Bubble Sort).
    Sorts a list of student tuple/list records based on a specified key.
    
    :param student_records: List of tuples e.g., [("STU1001", 85.5), ("STU1002", 92.0)]
    :param key_index: Index of element to sort by (default score index = 1)
    :param reverse: True for descending order (highest score first)
    :return: Sorted list of tuples
    """
    n = len(student_records)
    records = list(student_records) # Copy list
    
    for i in range(n):
        for j in range(0, n - i - 1):
            cond = (records[j][key_index] < records[j + 1][key_index]) if reverse else (records[j][key_index] > records[j + 1][key_index])
            if cond:
                records[j], records[j + 1] = records[j + 1], records[j]
                
    return records

if __name__ == "__main__":
    # Quick sanity test
    test_records = [("STU101", 72.5), ("STU102", 91.0), ("STU103", 64.0), ("STU104", 88.0)]
    sorted_recs = custom_bubble_sort_students(test_records, reverse=True)
    print("Sorted records by score:", sorted_recs)
