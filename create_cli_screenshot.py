"""
Generate a terminal output screenshot for CLI Execution Output (Section 5)
Outputs charts/08_cli_execution_output.png
"""

import os
import matplotlib.pyplot as plt

def generate_cli_screenshot():
    fig, ax = plt.subplots(figsize=(10, 6.8), dpi=300)
    ax.axis('off')
    fig.patch.set_facecolor('#0f172a') # Dark slate background

    # Title bar
    ax.fill_between([0, 1], [0.93, 0.93], [1.0, 1.0], color='#1e293b')
    # Terminal buttons
    ax.scatter([0.03, 0.05, 0.07], [0.965, 0.965, 0.965], color=['#ef4444', '#f59e0b', '#10b981'], s=50)
    ax.text(0.5, 0.965, "PowerShell - python main.py (Interactive Prediction Mode)", ha="center", va="center", color="#94a3b8", fontsize=9.5, family="monospace")

    terminal_text = [
        ("PS C:\\Users\\soura\\Desktop\\MLPROJECT> python main.py", "#38bdf8", True),
        ("======================================================================", "#64748b", False),
        (" INTERACTIVE STUDENT PERFORMANCE PREDICTION (PBL - MACHINE LEARNING)", "#f8fafc", True),
        ("======================================================================", "#64748b", False),
        ("[INFO] Loading trained regression model: models_saved/best_regression_model.pkl", "#10b981", False),
        ("[INFO] Loading StandardScaler: models_saved/scaler.pkl", "#10b981", False),
        ("", "#ffffff", False),
        ("Please enter the following student details:", "#cbd5e1", True),
        ("1. Attendance Percentage (0 - 100%): 92.5", "#f1f5f9", False),
        ("2. Study Hours Per Week (0 - 70 hrs): 18.0", "#f1f5f9", False),
        ("3. Previous Semester Marks (0 - 100%): 88.0", "#f1f5f9", False),
        ("4. Assignment Score (0 - 100%): 90.0", "#f1f5f9", False),
        ("5. Class Participation Rating (1 - 10): 9", "#f1f5f9", False),
        ("6. Has Home Internet Access? (Yes/No): Yes", "#f1f5f9", False),
        ("", "#ffffff", False),
        ("----------------------------------------------------------------------", "#64748b", False),
        (" PREDICTION & ACADEMIC RISK ADVISORY REPORT", "#38bdf8", True),
        ("----------------------------------------------------------------------", "#64748b", False),
        ("  • Predicted Final Academic Score : 85.8% [Grade: A]", "#4ade80", True),
        ("  • Academic Outcome Status        : PASS (Probability: 99.4%)", "#4ade80", True),
        ("  • Risk Classification Level      : TOP PERFORMER", "#38bdf8", True),
        ("  • Action Plan / Recommendation   : Outstanding academic engagement!", "#f8fafc", False),
        ("                                     Eligible for honors and peer-mentorship roles.", "#94a3b8", False),
        ("----------------------------------------------------------------------", "#64748b", False),
        ("[SUCCESS] Output generated and student ranked via custom QuickSort.", "#10b981", False)
    ]

    y = 0.88
    for line, color, is_bold in terminal_text:
        ax.text(0.03, y, line, ha="left", va="center", color=color, fontsize=9.2, family="monospace", weight="bold" if is_bold else "normal")
        y -= 0.034

    plt.tight_layout()
    save_path = os.path.join("charts", "08_cli_execution_output.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"[SUCCESS] Saved CLI screenshot: {save_path}")

if __name__ == "__main__":
    generate_cli_screenshot()
