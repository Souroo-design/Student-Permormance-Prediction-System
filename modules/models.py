"""
Machine Learning Models & Evaluation Module
Contains model training pipelines, metric evaluations, feature importance extraction,
and model persistence.
"""

import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

class ModelTrainer:
    """Class to handle training, evaluating, and saving ML models for student performance prediction."""
    
    def __init__(self, models_dir: str = "models_saved", charts_dir: str = "charts"):
        self.models_dir = models_dir
        self.charts_dir = charts_dir
        os.makedirs(self.models_dir, exist_ok=True)
        os.makedirs(self.charts_dir, exist_ok=True)
        
        self.best_reg_model = None
        self.best_clf_model = None
        self.feature_names = None

    def train_and_evaluate_regression(self, X_train, X_test, y_train, y_test, feature_names):
        """
        Trains and evaluates Multiple Linear Regression, Decision Tree, and Random Forest Regressors.
        Returns a comparative performance dictionary.
        """
        self.feature_names = feature_names
        
        reg_models = {
            "Linear Regression": LinearRegression(),
            "Ridge Regression": Ridge(alpha=1.0),
            "Decision Tree Regressor": DecisionTreeRegressor(max_depth=6, random_state=42),
            "Random Forest Regressor": RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42)
        }
        
        results = {}
        best_r2 = -float('inf')
        
        print("\n" + "="*60)
        print(" REGRESSION MODEL EVALUATION RESULTS (Predicting Final Score %)")
        print("="*60)
        
        for name, model in reg_models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            rmse = np.sqrt(mse)
            r2 = r2_score(y_test, y_pred)
            
            results[name] = {
                "MAE": mae,
                "MSE": mse,
                "RMSE": rmse,
                "R2_Score": r2,
                "model_obj": model,
                "predictions": y_pred
            }
            
            print(f"[{name}]")
            print(f"  - MAE: {mae:.3f} | RMSE: {rmse:.3f} | R² Score: {r2:.4f}")
            
            if r2 > best_r2:
                best_r2 = r2
                self.best_reg_model = model
                best_name = name
                best_preds = y_pred

        print("="*60)
        print(f"[BEST REGRESSION MODEL]: {best_name} (R² = {best_r2:.4f})\n")
        
        # Save best regression model
        reg_model_path = os.path.join(self.models_dir, "best_regression_model.pkl")
        joblib.dump(self.best_reg_model, reg_model_path)
        print(f"[MODEL SAVED] Best regression model saved to: {reg_model_path}")
        
        # Plot Actual vs Predicted for Best Model
        self._plot_actual_vs_predicted(y_test, best_preds, best_name)
        
        # Plot Feature Importance if RF or DT
        if hasattr(self.best_reg_model, "feature_importances_"):
            self._plot_feature_importance(self.best_reg_model.feature_importances_, feature_names, best_name)
        elif hasattr(self.best_reg_model, "coef_"):
            self._plot_feature_importance(np.abs(self.best_reg_model.coef_), feature_names, best_name)

        return results

    def train_and_evaluate_classification(self, X_train, X_test, y_train, y_test):
        """
        Trains and evaluates Logistic Regression and Random Forest Classifiers for Pass/Fail prediction.
        """
        clf_models = {
            "Logistic Regression": LogisticRegression(random_state=42),
            "Random Forest Classifier": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
        }
        
        results = {}
        best_f1 = -float('inf')
        
        print("\n" + "="*60)
        print(" CLASSIFICATION MODEL EVALUATION RESULTS (Predicting Pass/Fail)")
        print("="*60)
        
        for name, model in clf_models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            acc = accuracy_score(y_test, y_pred)
            prec = precision_score(y_test, y_pred)
            rec = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
            
            results[name] = {
                "Accuracy": acc,
                "Precision": prec,
                "Recall": rec,
                "F1_Score": f1,
                "Confusion_Matrix": cm,
                "model_obj": model
            }
            
            print(f"[{name}]")
            print(f"  - Accuracy: {acc*100:.2f}% | Precision: {prec:.3f} | Recall: {rec:.3f} | F1-Score: {f1:.3f}")
            
            if f1 > best_f1:
                best_f1 = f1
                self.best_clf_model = model
                best_name = name
                best_cm = cm
                
        print("="*60)
        print(f"[BEST CLASSIFICATION MODEL]: {best_name} (F1 = {best_f1:.4f})\n")
        
        # Save best classification model
        clf_model_path = os.path.join(self.models_dir, "best_classification_model.pkl")
        joblib.dump(self.best_clf_model, clf_model_path)
        print(f"[MODEL SAVED] Best classification model saved to: {clf_model_path}")
        
        # Plot Confusion Matrix
        self._plot_confusion_matrix(best_cm, best_name)
        
        return results

    def _plot_actual_vs_predicted(self, y_actual, y_pred, model_name):
        """Plots Scatter diagram of Actual vs Predicted final scores."""
        plt.figure(figsize=(8, 6))
        plt.scatter(y_actual, y_pred, alpha=0.6, color='#2980b9', edgecolors='k')
        plt.plot([y_actual.min(), y_actual.max()], [y_actual.min(), y_actual.max()], 'r--', lw=2, label='Ideal 1:1 Match')
        plt.title(f'Actual vs Predicted Scores ({model_name})', fontsize=14, fontweight='bold', pad=12)
        plt.xlabel('Actual Final Score (%)', fontsize=12)
        plt.ylabel('Predicted Final Score (%)', fontsize=12)
        plt.legend()
        plt.tight_layout()
        
        save_path = os.path.join(self.charts_dir, "05_actual_vs_predicted.png")
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"[PLOTS] Saved Actual vs Predicted plot to: {save_path}")

    def _plot_feature_importance(self, importances, feature_names, model_name):
        """Plots feature importance bar chart."""
        feat_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': importances
        }).sort_values('Importance', ascending=True)
        
        plt.figure(figsize=(9, 5))
        plt.barh(feat_df['Feature'], feat_df['Importance'], color='#16a085', edgecolor='black')
        plt.title(f'Feature Importance / Weights ({model_name})', fontsize=14, fontweight='bold', pad=12)
        plt.xlabel('Relative Importance Weight', fontsize=12)
        plt.tight_layout()
        
        save_path = os.path.join(self.charts_dir, "06_feature_importance.png")
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"[PLOTS] Saved Feature Importance plot to: {save_path}")

    def _plot_confusion_matrix(self, cm, model_name):
        """Plots heatmap confusion matrix for classification."""
        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=['Fail', 'Pass'], yticklabels=['Fail', 'Pass'])
        plt.title(f'Confusion Matrix ({model_name})', fontsize=14, fontweight='bold', pad=12)
        plt.xlabel('Predicted Label', fontsize=12)
        plt.ylabel('Actual True Label', fontsize=12)
        plt.tight_layout()
        
        save_path = os.path.join(self.charts_dir, "07_confusion_matrix.png")
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"[PLOTS] Saved Confusion Matrix plot to: {save_path}")
