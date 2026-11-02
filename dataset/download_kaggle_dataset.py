"""
KaggleHub Dataset Downloader for Student Performance Prediction System
Fetches the Student Performance dataset directly from Kaggle Hub using kagglehub.
"""

import os
import kagglehub
import pandas as pd
import numpy as np

KAGGLE_DATASET_HANDLE = "nikhil7280/student-performance-multiple-linear-regression"

def fetch_and_prepare_kaggle_dataset(output_dir="dataset"):
    """
    Downloads dataset from Kaggle Hub using kagglehub.dataset_download(),
    standardizes column names, derives Pass/Fail & Grade targets, and saves to student_data.csv.
    """
    print(f"[INFO] Fetching dataset from Kaggle Hub: '{KAGGLE_DATASET_HANDLE}'...")
    
    # 1. Download dataset via kagglehub
    download_path = kagglehub.dataset_download(KAGGLE_DATASET_HANDLE)
    print(f"[SUCCESS] KaggleHub download complete. Cached at: {download_path}")
    
    # 2. Locate CSV file
    csv_files = [f for f in os.listdir(download_path) if f.endswith('.csv')]
    if not csv_files:
        raise FileNotFoundError(f"No CSV file found in Kaggle download path: {download_path}")
        
    csv_filepath = os.path.join(download_path, csv_files[0])
    print(f"[INFO] Reading CSV file: {csv_filepath}")
    df_raw = pd.read_csv(csv_filepath)
    
    # 3. Rename columns to standard internal names
    column_mapping = {
        'Hours Studied': 'Study_Hours_Per_Week',
        'Previous Scores': 'Previous_Marks',
        'Sample Question Papers Practiced': 'Assignment_Score',
        'Performance Index': 'Final_Score'
    }
    df = df_raw.rename(columns=column_mapping)
    
    # 4. Add additional rich behavioral attributes for realistic EDA & modeling
    num_rows = len(df)
    np.random.seed(42)
    
    # Attendance: Strongly correlated with previous scores + study hours + noise
    attendance = np.clip(0.5 * df['Previous_Marks'] + 1.5 * df['Study_Hours_Per_Week'] + np.random.normal(30, 8, num_rows), 42.0, 100.0).round(1)
    df['Attendance_Percentage'] = attendance
    
    # Participation Rating: 1 to 10 scale
    df['Class_Participation'] = np.clip(np.random.normal(6.5, 1.8, num_rows), 1, 10).round().astype(int)
    
    # Internet Access
    df['Internet_Access'] = np.random.choice(["Yes", "No"], size=num_rows, p=[0.85, 0.15])
    
    # Re-scale Assignment Score to 0-100 percentage range for consistency
    df['Assignment_Score'] = (df['Assignment_Score'] * 9.5 + 5.0).clip(20.0, 100.0).round(1)
    
    # 5. Derive Pass/Fail and Grade targets
    df['Pass_Fail'] = np.where(df['Final_Score'] >= 50.0, 'Pass', 'Fail')
    
    grades = []
    for score in df['Final_Score']:
        if score >= 80.0:
            grades.append("A")
        elif score >= 70.0:
            grades.append("B")
        elif score >= 60.0:
            grades.append("C")
        elif score >= 50.0:
            grades.append("D")
        else:
            grades.append("F")
    df['Grade'] = grades
    
    # Generate Student_ID column
    df.insert(0, 'Student_ID', [f"STU{10000 + i}" for i in range(num_rows)])
    
    # 6. Introduce ~2% missing values in Attendance & Previous Marks for Data Cleaning syllabus requirement
    mask_att = np.random.rand(num_rows) < 0.02
    df.loc[mask_att, "Attendance_Percentage"] = np.nan
    
    mask_prev = np.random.rand(num_rows) < 0.015
    df.loc[mask_prev, "Previous_Marks"] = np.nan
    
    # Rearrange column order (excluding Sleep_Hours, Extracurricular_Activities, Parental_Education)
    cols_order = [
        "Student_ID", "Attendance_Percentage", "Study_Hours_Per_Week", "Previous_Marks",
        "Assignment_Score", "Class_Participation", "Internet_Access",
        "Final_Score", "Pass_Fail", "Grade"
    ]
    df = df[cols_order]
    
    # 7. Save to dataset directory
    os.makedirs(output_dir, exist_ok=True)
    out_filepath = os.path.join(output_dir, "student_data.csv")
    df.to_csv(out_filepath, index=False)
    data_csv_filepath = os.path.join(output_dir, "data.csv")
    df.to_csv(data_csv_filepath, index=False)
    print(f"[SUCCESS] Prepared Kaggle dataset with {len(df)} records saved to: {out_filepath}")
    return df

if __name__ == "__main__":
    fetch_and_prepare_kaggle_dataset()
