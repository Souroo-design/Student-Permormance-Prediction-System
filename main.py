"""
Main CLI Application for Student Performance Prediction System
Project-Based Learning (PBL) Implementation
"""

import os
import sys
import joblib
import pandas as pd
import numpy as np

from modules.data_loader import DataLoader
from modules.preprocessing import DataPreprocessor
from modules.eda import ExploratoryDataAnalysis
from modules.models import ModelTrainer
from modules.utils import categorize_risk_status, validate_student_input, custom_quick_sort

DATASET_PATH = os.path.join("dataset", "student_data.csv")

def run_training_pipeline():
    """Executes full Data Loading -> Preprocessing -> EDA -> Model Training workflow."""
    print("\n" + "="*70)
    print(" STEP 1: LOADING DATASET")
    print("="*70)
    loader = DataLoader(DATASET_PATH)
    df = loader.load_data()
    
    print("\n" + "="*70)
    print(" STEP 2: DATA PREPROCESSING & FEATURE ENGINEERING")
    print("="*70)
    preprocessor = DataPreprocessor()
    X, y_reg, y_clf = preprocessor.prepare_features_and_targets(df)
    
    # Train-test split (80-20 split)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_reg_train, y_reg_test = train_test_split(X, y_reg, test_size=0.2, random_state=42)
    _, _, y_clf_train, y_clf_test = train_test_split(X, y_clf, test_size=0.2, random_state=42)
    
    # Scaling features
    X_train_scaled = preprocessor.fit_transform_scaling(X_train)
    X_test_scaled = preprocessor.transform_scaling(X_test)
    
    # Ensure models_saved directory exists
    os.makedirs("models_saved", exist_ok=True)
    os.makedirs("charts", exist_ok=True)
    
    scaler_path = os.path.join("models_saved", "scaler.pkl")
    joblib.dump(preprocessor.scaler, scaler_path)
    print(f"[PREPROCESSING] Scaler saved to: {scaler_path}")
    
    print("\n" + "="*70)
    print(" STEP 3: EXPLORATORY DATA ANALYSIS (EDA)")
    print("="*70)
    eda = ExploratoryDataAnalysis(df)
    eda.generate_all_plots()
    
    print("\n" + "="*70)
    print(" STEP 4: MODEL TRAINING & COMPARATIVE EVALUATION")
    print("="*70)
    trainer = ModelTrainer()
    reg_results = trainer.train_and_evaluate_regression(X_train_scaled, X_test_scaled, y_reg_train, y_reg_test, preprocessor.feature_columns)
    clf_results = trainer.train_and_evaluate_classification(X_train_scaled, X_test_scaled, y_clf_train, y_clf_test)
    
    print("\n[SUCCESS] Pipeline execution complete! All plots exported to 'charts/' and models saved to 'models_saved/'.")

def interactive_prediction_mode():
    """Allows user to enter custom student parameters and predict expected performance."""
    print("\n" + "="*70)
    print(" INTERACTIVE STUDENT PERFORMANCE PREDICTION")
    print("="*70)
    
    reg_path = os.path.join("models_saved", "best_regression_model.pkl")
    scaler_path = os.path.join("models_saved", "scaler.pkl")
    
    if not (os.path.exists(reg_path) and os.path.exists(scaler_path)):
        print("[WARNING] Trained models not found. Running training pipeline first...")
        run_training_pipeline()
        
    model = joblib.load(reg_path)
    scaler = joblib.load(scaler_path)
    
    print("Please enter the following student details:\n")
    try:
        att = float(input("1. Attendance Percentage (0 - 100%): "))
        study = float(input("2. Study Hours Per Week (0 - 70 hrs): "))
        prev = float(input("3. Previous Semester Marks (0 - 100%): "))
        assign = float(input("4. Assignment Score (0 - 100%): "))
        part = int(input("5. Class Participation Rating (1 - 10): "))
        internet_str = input("6. Has Home Internet Access? (Yes/No): ").strip().capitalize()
        
        # Validation
        is_valid, msg = validate_student_input(att, study, prev, assign, part)
        if not is_valid:
            print(f"\n[INPUT ERROR] {msg}")
            return
            
        # Encoding categorical variables
        internet_num = 1 if internet_str == 'Yes' else 0
        
        # Array creation
        input_data = np.array([[att, study, prev, assign, part, internet_num]])
        input_scaled = scaler.transform(input_data)
        
        # Predict
        predicted_score = float(model.predict(input_scaled)[0])
        predicted_score = np.clip(predicted_score, 0.0, 100.0)
        
        # Risk assessment using Python conditions
        result = categorize_risk_status(predicted_score, att, study)
        
        print("\n" + "*"*50)
        print(" PREDICTION RESULT SUMMARY")
        print("*"*50)
        print(f" Predicted Final Score : {result['predicted_score']:.2f}%")
        print(f" Expected Grade        : {result['grade']}")
        print(f" Status                : {result['pass_fail']}")
        print(f" Risk Categorization   : {result['risk_level']}")
        print(f" Actionable Guidance   : {result['action_plan']}")
        print("*"*50 + "\n")
        
    except ValueError:
        print("[ERROR] Invalid numeric input entered. Please try again with valid numbers.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred during prediction: {e}")

def custom_sorting_demonstration():
    """Demonstrates manual QuickSort algorithm on student records (Syllabus topic)."""
    print("\n" + "="*70)
    print(" DEMONSTRATION: CUSTOM QUICKSORT ALGORITHM ON STUDENT RECORDS")
    print("="*70)
    
    loader = DataLoader(DATASET_PATH)
    df = loader.load_data()
    
    # Extract records as list of tuples: (Student_ID, Final_Score, Attendance_Percentage)
    records = list(zip(df['Student_ID'], df['Final_Score'], df['Attendance_Percentage']))
    
    print("\nSorting top 10 students by Final Score (Descending) using Custom QuickSort...")
    sorted_records = custom_quick_sort(records, key_index=1, reverse=True)
    
    print(f"{'Rank':<6} | {'Student ID':<12} | {'Final Score (%)':<18} | {'Attendance (%)':<15}")
    print("-" * 60)
    for rank, rec in enumerate(sorted_records[:10], 1):
        print(f"{rank:<6} | {rec[0]:<12} | {rec[1]:<18.2f} | {rec[2]:<15.1f}")
    print("-" * 60)

def main_menu():
    """Main interactive terminal interface."""
    while True:
        print("\n=======================================================")
        print("    STUDENT PERFORMANCE PREDICTION SYSTEM")
        print("=======================================================")
        print(" 1. Run ML Pipeline (Train Models & Export EDA Plots)")
        print(" 2. Predict Performance for a New Student (Interactive)")
        print(" 3. View Top Performing Students (Custom QuickSort Demo)")
        print(" 4. Exit")
        print("=======================================================")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            run_training_pipeline()
        elif choice == '2':
            interactive_prediction_mode()
        elif choice == '3':
            custom_sorting_demonstration()
        elif choice == '4':
            print("\nExiting Student Performance Prediction System. Good luck with your PBL presentation!")
            sys.exit(0)
        else:
            print("[INVALID CHOICE] Please enter a valid number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
