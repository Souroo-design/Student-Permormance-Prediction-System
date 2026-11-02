"""
Exploratory Data Analysis (EDA) Module
Generates high-resolution visualizations for statistical insight and exports them to charts/
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set modern aesthetic style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 1.0

class ExploratoryDataAnalysis:
    """Class to perform EDA and output figures for reports and analysis."""
    
    def __init__(self, df: pd.DataFrame, output_dir: str = "charts"):
        self.df = df.copy()
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def plot_target_distribution(self):
        """Plots distribution of Final Scores and Pass/Fail counts."""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Plot 1: Histogram of Final Scores
        sns.histplot(self.df['Final_Score'].dropna(), kde=True, color='#2b5c8f', ax=axes[0], bins=20)
        axes[0].set_title('Distribution of Student Final Scores', fontsize=14, fontweight='bold', pad=10)
        axes[0].set_xlabel('Final Score (%)', fontsize=12)
        axes[0].set_ylabel('Student Count', fontsize=12)
        axes[0].axvline(self.df['Final_Score'].mean(), color='#e74c3c', linestyle='--', label=f"Mean: {self.df['Final_Score'].mean():.1f}%")
        axes[0].legend()

        # Plot 2: Pass/Fail Pie Chart
        pass_counts = self.df['Pass_Fail'].value_counts()
        colors = ['#2ecc71', '#e74c3c']
        axes[1].pie(pass_counts, labels=pass_counts.index, autopct='%1.1f%%', colors=colors, startangle=140, explode=(0.05, 0), textprops={'fontsize': 12})
        axes[1].set_title('Pass vs Fail Proportion', fontsize=14, fontweight='bold', pad=10)

        plt.tight_layout()
        save_path = os.path.join(self.output_dir, "01_score_distribution.png")
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"[EDA] Saved distribution plot to: {save_path}")

    def plot_correlation_heatmap(self):
        """Generates correlation heatmap of numeric features."""
        plt.figure(figsize=(10, 8))
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        corr_matrix = self.df[numeric_cols].corr()

        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Pearson Correlation'})
        plt.title('Feature Correlation Heatmap', fontsize=14, fontweight='bold', pad=12)
        plt.tight_layout()

        save_path = os.path.join(self.output_dir, "02_correlation_heatmap.png")
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"[EDA] Saved correlation heatmap to: {save_path}")

    def plot_study_hours_vs_score(self):
        """Plots Study Hours vs Final Score with regression trendline."""
        plt.figure(figsize=(8, 6))
        sns.regplot(data=self.df, x='Study_Hours_Per_Week', y='Final_Score', scatter_kws={'alpha': 0.6, 'color': '#3498db'}, line_kws={'color': '#e74c3c', 'linewidth': 2})
        plt.title('Study Hours per Week vs Final Score', fontsize=14, fontweight='bold', pad=12)
        plt.xlabel('Study Hours / Week', fontsize=12)
        plt.ylabel('Final Score (%)', fontsize=12)
        plt.tight_layout()

        save_path = os.path.join(self.output_dir, "03_study_vs_score.png")
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"[EDA] Saved Study Hours vs Score scatter plot to: {save_path}")

    def plot_attendance_vs_score(self):
        """Plots Attendance Percentage vs Final Score with trendline."""
        plt.figure(figsize=(8, 6))
        sns.regplot(data=self.df, x='Attendance_Percentage', y='Final_Score', scatter_kws={'alpha': 0.6, 'color': '#27ae60'}, line_kws={'color': '#e74c3c', 'linewidth': 2})
        plt.title('Attendance Percentage vs Final Score', fontsize=14, fontweight='bold', pad=12)
        plt.xlabel('Attendance Percentage (%)', fontsize=12)
        plt.ylabel('Final Score (%)', fontsize=12)
        plt.tight_layout()

        save_path = os.path.join(self.output_dir, "04_attendance_vs_score.png")
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"[EDA] Saved Attendance vs Score plot to: {save_path}")

    def generate_all_plots(self):
        """Runs full EDA visual suite."""
        self.plot_target_distribution()
        self.plot_correlation_heatmap()
        self.plot_study_hours_vs_score()
        self.plot_attendance_vs_score()
        print("[EDA] All EDA visualizations generated successfully!")

if __name__ == "__main__":
    from data_loader import DataLoader
    loader = DataLoader("../dataset/student_data.csv")
    df = loader.load_data()
    eda = ExploratoryDataAnalysis(df, "../charts")
    eda.generate_all_plots()
