# Student Performance Prediction System (PBL Machine Learning)

## Project Overview
This project is developed for **PBL - Machine Learning (Student Performance Prediction)**. It predicts student academic performance (Final Score % and Pass/Fail status) based on key academic and behavioral factors such as attendance, study hours, previous marks, assignment scores, participation, and home internet access.

---

## 📦 PBL Submission Deliverables

As per PBL submission requirements, this repository contains all 3 mandatory deliverables:

1. **Application / Project**:
   * Complete runnable Python source code: [`main.py`](file:///c:/Users/soura/OneDrive/Desktop/MLPROJECT/main.py) with interactive CLI.
   * Modular architecture: [`modules/`](file:///c:/Users/soura/OneDrive/Desktop/MLPROJECT/modules) (`data_loader.py`, `preprocessing.py`, `eda.py`, `models.py`, `utils.py`).
   * Benchmark dataset & automated downloader: [`dataset/`](file:///c:/Users/soura/OneDrive/Desktop/MLPROJECT/dataset).
   * Pre-trained models: [`models_saved/`](file:///c:/Users/soura/OneDrive/Desktop/MLPROJECT/models_saved).
2. **Project Documentation**:
   * Complete formal report document: [`Student_Performance_Prediction_Report.docx`](file:///c:/Users/soura/OneDrive/Desktop/MLPROJECT/Student_Performance_Prediction_Report.docx).
   * Detailed architectural and algorithm documentation: [`PROJECT_DOCUMENTATION.md`](file:///c:/Users/soura/OneDrive/Desktop/MLPROJECT/PROJECT_DOCUMENTATION.md).
3. **Presentation (PPT)**:
   * Professional slides for final evaluation: [`Student_Performance_Prediction_Presentation.pptx`](file:///c:/Users/soura/OneDrive/Desktop/MLPROJECT/Student_Performance_Prediction_Presentation.pptx).

---

## 📁 Workspace Directory Structure

```text
MLPROJECT/
├── dataset/
│   ├── download_kaggle_dataset.py   # KaggleHub dataset downloader (kagglehub)
│   └── student_data.csv            # 10,000 record Kaggle student dataset
├── modules/
│   ├── __init__.py
│   ├── data_loader.py              # File handling, OOP loading, Exception handling
│   ├── preprocessing.py            # Data cleaning, median imputation & scaling
│   ├── eda.py                      # Matplotlib & Seaborn visualization pipeline
│   ├── models.py                   # Linear Regression, Decision Tree, Random Forest
│   └── utils.py                    # Risk conditions, range validation & QuickSort
├── models_saved/
│   ├── best_regression_model.pkl   # Trained regression model binary (R² = 96.93%)
│   ├── best_classification_model.pkl # Trained Pass/Fail model binary
│   └── scaler.pkl                  # Standard Scaler object
├── charts/                         # Auto-exported high-res visualization plots
│   ├── 01_score_distribution.png
│   ├── 02_correlation_heatmap.png
│   ├── 03_study_vs_score.png
│   ├── 04_attendance_vs_score.png
│   ├── 05_actual_vs_predicted.png
│   ├── 06_feature_importance.png
│   ├── 07_confusion_matrix.png
│   └── 08_cli_execution_output.png
├── main.py                         # Command Line Interface (CLI) application
├── requirements.txt                # Required Python packages
├── README.md                       # Project setup & execution guide
└── PROJECT_REPORT.md               # Complete printable project report template
```

---

## 🚀 How to Run the Project in VS Code

### 1. Open Terminal in VS Code
Open VS Code and press ``Ctrl + ` ``.

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

### 3. Run Application
```bash
python main.py
```

---

## 📚 Syllabus Concepts Demonstrated in Code

| Syllabus Requirement | Module / Implementation | Description |
| :--- | :--- | :--- |
| **Conditions** | `modules/utils.py` | Multi-factor `if-elif-else` branches for grade assignment and risk level classification. |
| **Loops** | `modules/preprocessing.py`, `main.py` | `for` and `while` loops for feature processing, range validations, menu options. |
| **Collections** | `modules/data_loader.py`, `modules/utils.py` | Dictionaries, lists, and tuples for student records and metrics. |
| **Functions & OOP** | `modules/*.py` | Classes like `DataLoader`, `DataPreprocessor`, `ModelTrainer`, `ExploratoryDataAnalysis`. |
| **Sorting** | `modules/utils.py` | Manual `custom_quick_sort()` algorithm implementation. |
| **File Handling** | `modules/data_loader.py` | `try-except` reading CSV dataset and writing model pickles via `joblib`. |
| **Exception Handling**| `modules/utils.py` | `try-except-finally` blocks for data range validation and input safety. |
| **NumPy & Pandas** | `modules/preprocessing.py` | DataFrame filtering, median imputation, matrix scaling, statistics. |
| **Matplotlib / Seaborn**| `modules/eda.py` | Histograms, heatmaps, scatter plots, boxplots exported to `charts/`. |

---

## 📊 Key Machine Learning Results

- **Best Regression Model**: Random Forest Regressor ($R^2 = 0.9693$, MAE = 2.18%) / Linear Regression ($R^2 = 0.9663$, MAE = 2.09%)
- **Pass/Fail Classification**: Logistic Regression (Accuracy = 96.60%, $F_1$-Score = 0.9712)
- **Top Predictive Factors**:
  1. Previous Semester Marks (Weight ~ 85.1%)
  2. Study Hours per Week (Weight ~ 14.3%)
  3. Attendance Percentage (Weight ~ 0.5%)
