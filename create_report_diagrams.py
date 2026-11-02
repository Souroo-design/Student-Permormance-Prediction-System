"""
Generate Architectural and Data Flow Diagrams for the Project Documentation Report
Outputs clean, professional figures matching the sample report style.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("charts", exist_ok=True)

def generate_fig_3_1():
    """Generates Fig 3.1: Module and Data Flow Diagram"""
    fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
    ax.axis('off')
    
    # Background
    fig.patch.set_facecolor('#ffffff')
    
    # Box styles
    box_blue = dict(boxstyle="round,pad=0.5", fc="#2563EB", ec="#1D4ED8", lw=1.5)
    box_light = dict(boxstyle="round,pad=0.5", fc="#EFF6FF", ec="#93C5FD", lw=1.5)
    box_green = dict(boxstyle="round,pad=0.5", fc="#10B981", ec="#059669", lw=1.5)
    box_amber = dict(boxstyle="round,pad=0.5", fc="#F59E0B", ec="#D97706", lw=1.5)
    box_dark = dict(boxstyle="round,pad=0.5", fc="#1E293B", ec="#0F172A", lw=1.5)

    # Nodes
    ax.text(0.5, 0.94, "Start / System Launch\n(main.py Execution)", ha="center", va="center", color="white", weight="bold", fontsize=11, bbox=box_dark)
    
    ax.text(0.5, 0.81, "1. Data Loading Module (data_loader.py)\n[Reads student_data.csv / KaggleHub Dataset Ingestion]", ha="center", va="center", color="white", weight="bold", fontsize=10.5, bbox=box_blue)
    
    ax.text(0.5, 0.67, "2. Preprocessing & Cleaning Module (preprocessing.py)\n[Median Missing Value Imputation | Binary Encoding | StandardScaler Z-Score]", ha="center", va="center", color="#1E3A8A", weight="bold", fontsize=10, bbox=box_light)
    
    ax.text(0.5, 0.53, "3. Exploratory Data Analysis Module (eda.py)\n[Distribution Histograms | Pearson Correlation Heatmap | Scatter Regressions]", ha="center", va="center", color="#1E3A8A", weight="bold", fontsize=10, bbox=box_light)
    
    # Dual Branches for Models
    ax.text(0.26, 0.38, "Regression Models\n• Linear Regression (Best)\n• Ridge Regression\n• Random Forest Regressor\n• Decision Tree Regressor", ha="center", va="center", color="white", weight="bold", fontsize=9.5, bbox=box_blue)
    ax.text(0.74, 0.38, "Classification Models\n• Logistic Regression (Best)\n• Random Forest Classifier\n• Pass/Fail Binary Target\n• Evaluation Metrics: F1, Acc", ha="center", va="center", color="white", weight="bold", fontsize=9.5, bbox=box_green)

    ax.text(0.5, 0.23, "5. Model Persistence & Serialization\n[Exports best_regression_model.pkl, best_classification_model.pkl & scaler.pkl]", ha="center", va="center", color="white", weight="bold", fontsize=10, bbox=box_amber)

    ax.text(0.5, 0.08, "6. Interactive CLI & Academic Risk Profiler (utils.py)\n[Real-time Student Prediction, Grade Assignment & 4-Tier Risk Action Plan]", ha="center", va="center", color="white", weight="bold", fontsize=10.5, bbox=box_dark)

    # Arrows
    arrow_props = dict(arrowstyle="->", lw=2, color="#475569")
    ax.annotate("", xy=(0.5, 0.86), xytext=(0.5, 0.89), arrowprops=arrow_props)
    ax.annotate("", xy=(0.5, 0.73), xytext=(0.5, 0.76), arrowprops=arrow_props)
    ax.annotate("", xy=(0.5, 0.59), xytext=(0.5, 0.61), arrowprops=arrow_props)
    
    # Split arrows
    ax.annotate("", xy=(0.26, 0.45), xytext=(0.42, 0.48), arrowprops=arrow_props)
    ax.annotate("", xy=(0.74, 0.45), xytext=(0.58, 0.48), arrowprops=arrow_props)
    
    # Rejoin arrows
    ax.annotate("", xy=(0.44, 0.28), xytext=(0.26, 0.31), arrowprops=arrow_props)
    ax.annotate("", xy=(0.56, 0.28), xytext=(0.74, 0.31), arrowprops=arrow_props)
    
    # Final arrow
    ax.annotate("", xy=(0.5, 0.13), xytext=(0.5, 0.18), arrowprops=arrow_props)

    plt.tight_layout()
    save_path = os.path.join("charts", "fig_3_1_data_flow.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] Saved Fig 3.1: {save_path}")

def generate_fig_3_2():
    """Generates Fig 3.2: Component Architecture Diagram"""
    fig, ax = plt.subplots(figsize=(10, 7.5), dpi=300)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Layer Cards
    # Presentation Layer
    p_box = dict(boxstyle="round,pad=0.4", fc="#F8FAFC", ec="#CBD5E1", lw=1.5)
    
    ax.text(0.5, 0.94, "PRESENTATION & INTERFACE LAYER", ha="center", va="center", color="#0F172A", weight="bold", fontsize=12)
    ax.text(0.5, 0.86, "main.py (Command Line Interface & Pipeline Orchestrator)\n[Option 1: Pipeline Train & Eval | Option 2: Interactive Real-Time Prediction]", ha="center", va="center", color="white", weight="bold", fontsize=10.5, bbox=dict(boxstyle="round,pad=0.5", fc="#1E293B", ec="#0F172A", lw=1.5))

    # Application Logic Layer
    ax.text(0.5, 0.72, "APPLICATION & MODULE PROCESSING LAYER", ha="center", va="center", color="#0F172A", weight="bold", fontsize=12)
    
    m_boxes = [
        ("data_loader.py\nFile Loader\n& KaggleHub API", 0.12, "#2563EB"),
        ("preprocessing.py\nImputer, Encoder\n& StandardScaler", 0.31, "#0EA5E9"),
        ("eda.py\nVisual Engine\n(Plots & Heatmaps)", 0.50, "#10B981"),
        ("models.py\nRegression &\nClassification", 0.69, "#F59E0B"),
        ("utils.py\nValidation, Sorting\n& Risk Profiler", 0.88, "#8B5CF6")
    ]
    for text, x_pos, col in m_boxes:
        ax.text(x_pos, 0.58, text, ha="center", va="center", color="white", weight="bold", fontsize=9, bbox=dict(boxstyle="round,pad=0.4", fc=col, ec=col, lw=1))

    # Machine Learning & Scientific Computing Core
    ax.text(0.5, 0.44, "SCIENTIFIC COMPUTING & ML FRAMEWORK CORE", ha="center", va="center", color="#0F172A", weight="bold", fontsize=12)
    frameworks = [
        ("NumPy\nArray Math", 0.18, "#EFF6FF", "#2563EB"),
        ("Pandas\nDataFrames", 0.39, "#EFF6FF", "#2563EB"),
        ("Scikit-Learn\nEstimators & Metrics", 0.61, "#EFF6FF", "#2563EB"),
        ("Matplotlib / Seaborn\nVisual Suite", 0.82, "#EFF6FF", "#2563EB")
    ]
    for text, x_pos, bg, fg in frameworks:
        ax.text(x_pos, 0.34, text, ha="center", va="center", color=fg, weight="bold", fontsize=9.5, bbox=dict(boxstyle="round,pad=0.4", fc=bg, ec=fg, lw=1.5))

    # Storage Layer
    ax.text(0.5, 0.20, "STORAGE & PERSISTENCE LAYER", ha="center", va="center", color="#0F172A", weight="bold", fontsize=12)
    storage = [
        ("dataset/student_data.csv\n(10,000 Records Dataset)", 0.25, "#1E293B"),
        ("models_saved/*.pkl\n(Trained Model & Scaler)", 0.50, "#1E293B"),
        ("charts/*.png\n(High-Res Visualizations)", 0.75, "#1E293B")
    ]
    for text, x_pos, col in storage:
        ax.text(x_pos, 0.09, text, ha="center", va="center", color="white", weight="bold", fontsize=9.5, bbox=dict(boxstyle="round,pad=0.4", fc=col, ec="#334155", lw=1.5))

    # Flow arrows
    arrow_props = dict(arrowstyle="<->", lw=2, color="#64748B")
    ax.annotate("", xy=(0.5, 0.77), xytext=(0.5, 0.81), arrowprops=arrow_props)
    ax.annotate("", xy=(0.5, 0.48), xytext=(0.5, 0.51), arrowprops=arrow_props)
    ax.annotate("", xy=(0.5, 0.24), xytext=(0.5, 0.28), arrowprops=arrow_props)

    plt.tight_layout()
    save_path = os.path.join("charts", "fig_3_2_system_architecture.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] Saved Fig 3.2: {save_path}")

def generate_fig_4_1():
    """Generates Fig 4.1: Data Model / Feature Schema Diagram"""
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Card 1: Features
    f_box = dict(boxstyle="round,pad=0.6", fc="#F8FAFC", ec="#2563EB", lw=2)
    features_text = (
        "FEATURE MATRIX (X: Predictor Attributes)\n"
        "──────────────────────────────────────────────\n"
        "• Attendance_Percentage  : Continuous Float  [0.0 - 100.0%]\n"
        "• Study_Hours_Per_Week   : Numerical Float   [0.0 - 70.0 hrs]\n"
        "• Previous_Marks         : Continuous Float  [0.0 - 100.0%]\n"
        "• Assignment_Score       : Continuous Float  [0.0 - 100.0%]\n"
        "• Class_Participation    : Discrete Integer  [1 - 10 Rating]\n"
        "• Internet_Access        : Binary Encoded    [1: Yes, 0: No]"
    )
    ax.text(0.27, 0.55, features_text, ha="center", va="center", color="#0F172A", fontsize=9.5, family="monospace", bbox=f_box)

    # Card 2: Targets
    t_box = dict(boxstyle="round,pad=0.6", fc="#F8FAFC", ec="#10B981", lw=2)
    targets_text = (
        "TARGET & DERIVED OUTPUTS\n"
        "──────────────────────────────────────────────\n"
        "1. Final_Score (y_reg)   : Continuous Float\n"
        "   Range: [0.0 - 100.0%]\n"
        "2. Pass_Fail (y_clf)     : Binary / Nominal\n"
        "   Values: 'Pass' (1) | 'Fail' (0)\n"
        "3. Grade                 : Ordinal Letter\n"
        "   Categories: A, B, C, D, F\n"
        "4. Risk_Status           : Categorical Advisory\n"
        "   Tiers: Top Performer, Low Risk,\n"
        "          Moderate Risk, High Risk"
    )
    ax.text(0.75, 0.55, targets_text, ha="center", va="center", color="#0F172A", fontsize=9.5, family="monospace", bbox=t_box)

    # Header and connector
    ax.text(0.5, 0.92, "STUDENT PERFORMANCE DATA MODEL & ATTRIBUTE SCHEMA", ha="center", va="center", color="#0F172A", weight="bold", fontsize=13)
    ax.text(0.5, 0.86, "Consumes 10,000 Records via pandas.read_csv('dataset/student_data.csv')", ha="center", va="center", color="#64748B", style="italic", fontsize=10.5)

    arrow_props = dict(arrowstyle="->", lw=2.5, color="#2563EB")
    ax.annotate("Transforms & Predicts", xy=(0.54, 0.55), xytext=(0.47, 0.55), arrowprops=arrow_props, ha="center", va="bottom", fontsize=10, weight="bold", color="#1D4ED8")

    # Bottom notes
    ax.text(0.5, 0.12, "Preprocessed via Median Imputation for Missing Values and StandardScaler Z-Score Normalization", ha="center", va="center", color="#334155", weight="bold", fontsize=10, bbox=dict(boxstyle="round,pad=0.4", fc="#EFF6FF", ec="#93C5FD", lw=1))

    plt.tight_layout()
    save_path = os.path.join("charts", "fig_4_1_data_model.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] Saved Fig 4.1: {save_path}")

if __name__ == "__main__":
    generate_fig_3_1()
    generate_fig_3_2()
    generate_fig_4_1()
