"""
Generate Project Documentation Report in Microsoft Word (.docx) format
Following the exact 20-page sample document structure from Brainware University.
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets padding for table cell."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_code_block(doc, code_text):
    """Adds a shaded monospace code box."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, "F1F5F9")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def build_word_document(output_path="Student_Performance_Prediction_Report.docx"):
    doc = Document()

    # Set 1-inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base styles setup
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(30, 41, 59)

    # Helper paragraph formatters
    def add_p(text, bold=False, italic=False, size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0, color=RGBColor(30, 41, 59)):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if text:
            run = p.add_run(text)
            run.bold = bold
            run.italic = italic
            run.font.size = Pt(size)
            run.font.color.rgb = color
        return p

    def add_sec_title(title_text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(14)
        run = p.add_run(title_text)
        run.bold = True
        run.font.size = Pt(15)
        run.font.color.rgb = RGBColor(15, 23, 42)
        return p

    def add_sub_title(title_text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(title_text)
        run.bold = True
        run.font.size = Pt(12.5)
        run.font.color.rgb = RGBColor(30, 41, 59)
        return p

    def add_fig_caption(caption_text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(14)
        run = p.add_run(caption_text)
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(71, 85, 105)

    def add_image_safe(img_path, width_inches=6.0, caption=""):
        if os.path.exists(img_path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(4)
            run = p.add_run()
            run.add_picture(img_path, width=Inches(width_inches))
            if caption:
                add_fig_caption(caption)

    # =========================================================================
    # PAGE 1: TITLE PAGE
    # =========================================================================
    p = add_p("SAPPS", bold=True, size=24, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=30, space_after=2)
    p = add_p("(Student Academic Performance Prediction System)", bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    
    p = add_p("A PROJECT REPORT", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    p = add_p("SUBMITTED BY", bold=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

    # Student Details Table
    table = doc.add_table(rows=2, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    col_widths = [Inches(1.5), Inches(1.6), Inches(1.6), Inches(1.8)]
    for row in table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    headers = ["Roll Number", "Registration Number", "Student Code", "Student Name"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        set_cell_background(cell, "E2E8F0")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(9.5)

    data = ["24103460035", "24103002816", "BWU/BCA/24/000", "SOURAV SANDHUKHAN"]
    for i, d in enumerate(data):
        cell = table.cell(1, i)
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(d)
        run.font.size = Pt(9.5)

    p = add_p("", space_after=24)
    p = add_p("Of in partial fulfillment for the award of the degree", italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    p = add_p("BACHELOR OF COMPUTER APPLICATION", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    p = add_p("IN", bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    p = add_p("DEPARTMENT OF COMPUTATIONAL SCIENCE", bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36)

    p = add_p("BRAINWARE UNIVERSITY", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    p = add_p("398, Ramkrishnapur Road, Barasat, North 24 Parganas, Kolkata - 700 125", size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)

    doc.add_page_break()

    # =========================================================================
    # PAGE 2: ACKNOWLEDGEMENT
    # =========================================================================
    add_sec_title("ACKNOWLEDGEMENT")

    add_p("We would like to express our heartfelt gratitude to the Management and Faculty of Brainware University for providing us with the opportunity, guidance, and resources required to successfully complete this project. Their continuous support and encouragement have played a vital role in shaping our learning experience.")

    add_p("We extend our sincere thanks to our esteemed project supervisor, Mr. Sourav Sandhukhan, Assistant Professor, whose constant guidance, valuable suggestions, and insightful feedback have been instrumental throughout the development of this project. His expertise, patience, and motivation helped us overcome challenges and understand the core machine learning concepts effectively.")

    add_p("We are also deeply thankful to Dr. Jayanta Aich, Head of the Department of Computational Sciences, for providing a supportive academic environment and the necessary facilities that enabled us to complete this work successfully.")

    add_p("Our sincere appreciation goes to all the faculty members of the Department of Computational Sciences for sharing their knowledge, advice, and encouragement during the course of our project. Their teachings have significantly contributed to strengthening our technical understanding and skills.")

    add_p("Finally, we express our profound gratitude to our families and friends, whose constant support, understanding, and motivation inspired us to stay committed and focused during every phase of this project. Without their encouragement, this achievement would not have been possible.")

    add_p("", space_after=36)
    p = add_p("SIGNATURE:--", bold=True, size=11, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=4)
    p = add_p("SOURAV SANDHUKHAN", bold=True, size=11, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=2)
    p = add_p("(BWU/BCA/24/000)", size=10.5, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=0)

    doc.add_page_break()

    # =========================================================================
    # PAGE 3: ABSTRACT
    # =========================================================================
    add_sec_title("ABSTRACT")

    add_p("The Student Academic Performance Prediction System (SAPPS) is a machine learning-based analytical application developed in Python that predicts student academic outcomes, calculates expected percentage scores, and identifies at-risk students during the active semester. The main objective of this project is to demonstrate the practical implementation of core Machine Learning workflows and Python curriculum principles while providing educational institutions with a proactive decision-support tool.")

    add_p("The system is developed using a modular, object-oriented architecture in which the end-to-end data pipeline is divided into distinct functional classes and modules: DataLoader for resilient file reading, DataPreprocessor for data cleaning and standard scaling, ExploratoryDataAnalysis for automated statistical visualizations, ModelTrainer for multi-algorithm regression and classification, and a utilities suite for academic risk categorization and custom sorting algorithms.")

    add_p("Supervised machine learning algorithms are utilized for dual-target prediction: Multiple Linear Regression, Ridge Regression, Decision Tree Regressors, and Random Forest Regressors are evaluated for continuous final score percentage prediction (0–100%), while Logistic Regression and Random Forest Classifiers are deployed for binary Pass/Fail classification. Random Forest Regressor achieved the highest predictive accuracy with an R² Score of 96.93% (with Multiple Linear Regression achieving R² = 96.63% and MAE of 2.09%), while Logistic Regression achieved 96.60% classification accuracy (F1-Score = 0.971).")

    add_p("The application processes 10,000 real-world student records sourced from Kaggle Hub, handling practical data quality challenges through median missing value imputation and Z-Score standardization. Furthermore, an automated academic risk profiler categorizes students into four actionable tiers (Top Performer, Low Risk, Moderate Risk, High Risk) and issues personalized counseling directives based on multi-factor rules.")

    add_p("Overall, the Student Academic Performance Prediction System reinforces core concepts of object-oriented programming, data preprocessing, exploratory data analysis, regression and classification modeling, exception handling, and custom sorting algorithms, while equipping academic mentors with an empirical, early-warning solution to enhance student retention and academic success.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 4: INDEX
    # =========================================================================
    add_sec_title("INDEX")

    index_items = [
        "❖  ACKNOWLEDGMENT",
        "❖  ABSTRACT",
        "❖  LIST OF FIGURE",
        "❖  LIST OF TABLE",
        "❖  LIST OF SCREENSHOTS",
        "1.  INTRODUCTION",
        "2.  LITERATURE SURVEY",
        "3.  SYSTEM ANALYSIS AND DESIGN",
        "4.  IMPLEMENTATION",
        "5.  OUTPUT SCREENSHOT",
        "6.  SOURCE CODE",
        "7.  TESTING AND DEBUGGING",
        "8.  CONCLUSION AND FUTURE ENHANCEMENT",
        "9.  REFERENCES"
    ]
    for item in index_items:
        p = add_p(item, bold=True if ("1." in item or "❖" in item) else False, size=11, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=8)

    doc.add_page_break()

    # =========================================================================
    # PAGE 5: 1. INTRODUCTION
    # =========================================================================
    add_sec_title("1. INTRODUCTION")

    add_p("In today's fast-paced world, technology and data-driven methodologies play a crucial role in improving the efficiency and quality of modern education. The traditional method of evaluating student performance often relies entirely on periodic midterms or final cumulative examinations. This post-examination assessment process frequently leaves educators unable to assist struggling students in time, resulting in course failures, lost credits, and increased student attrition. These challenges highlight the need for an automated, predictive, and proactive performance monitoring system.")

    add_p("The Student Academic Performance Prediction System (SAPPS) is an advanced Machine Learning application developed in Python to overcome the limitations of traditional, reactive academic evaluations. It provides a reliable analytical platform where faculty advisors and course instructors can forecast expected final academic scores, evaluate pass/fail probabilities, and detect academically vulnerable students well before final examinations occur.")

    add_p("The system is organized into multiple reusable, object-oriented modules to ensure smooth functioning. The Data Ingestion Module safely reads dataset records and interfaces with Kaggle Hub. The Preprocessing & Cleaning Module handles real-world missing values using statistical median imputation and normalizes features using StandardScaler. The Exploratory Data Analysis (EDA) Module produces high-resolution statistical plots, and the Model Training Module evaluates multiple regression and classification algorithms.")

    add_p("The development of this system involves the use of modern Python data science and machine learning libraries, including NumPy and Pandas for data manipulation, Scikit-Learn for algorithm training and evaluation metrics, and Matplotlib and Seaborn for statistical plotting. The complete workflow is encapsulated in an interactive Command Line Interface (CLI) application developed in main.py.")

    add_p("One of the major advantages of the Student Academic Performance Prediction System is its dual predictive capability and interpretability. Rather than operating as an unexplainable black box, the system extracts normalized beta coefficient weights to reveal precisely how attendance, weekly study hours, previous semester marks, and assignment diligence impact final performance. Because the code is built from modular, decoupled classes, new features or machine learning models can be added with minimal changes to existing code.")

    add_p("Furthermore, the system enhances academic mentoring by providing dynamic, multi-tier risk categorization. Based on multi-factor logical rules combining predicted scores and attendance levels, students are assigned personalized action plans—such as mandatory remedial classes for high-risk students or advanced peer-mentorship roles for top performers.")

    add_p("In conclusion, the Student Academic Performance Prediction System is a modern, data-driven solution that not only simplifies early student intervention for educational institutions but also reinforces core computer science concepts—object-oriented programming, data cleaning, feature engineering, predictive modeling, exception handling, and custom sorting algorithms.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 6: 2. LITERATURE SURVEY
    # =========================================================================
    add_sec_title("2. LITERATURE SURVEY")

    add_p("The Student Academic Performance Prediction System builds upon an established body of academic research in Educational Data Mining (EDM) and Learning Analytics. Earlier institutional approaches were typically based on static rule-based thresholds—such as mandatory 75% attendance cutoffs or isolated midterm marks—where educators manually flagged students based on single parameters without accounting for multivariate interactions.")

    add_p("Research into modern Educational Data Mining shows that student performance is governed by a complex interplay of cognitive, behavioral, and digital factors. Landmark studies by Romero & Ventura (2020) demonstrated that multi-variable machine learning models outperform traditional single-attribute heuristics by over 40% in predicting student grade distributions, proving that factors such as weekly study hours and continuous assignment submission correlate heavily with exam performance.")

    add_p("Studies by Cortez & Silva (2008) on predicting student failure in secondary education highlighted that combining prior semester academic achievements with real-time class participation yields the most accurate predictive models. Their comparative experiments revealed that while complex non-linear models like Random Forests provide strong generalization, Multiple Linear Regression provides unmatched mathematical interpretability, which is essential when explaining academic feedback to students and faculty.")

    add_p("Previous work in learning analytics has also emphasized the necessity of data cleaning and scaling. Academic datasets frequently contain missing attendance logs and unrecorded marks. Standardizing numeric attributes through Z-score normalization eliminates scale bias between disparate ranges (such as study hours spanning 0–70 hours versus marks spanning 0–100%), ensuring stable gradient descent and unbiased feature weighting.")

    add_p("Based on these established studies, the Student Academic Performance Prediction System is designed as an end-to-end Python machine learning pipeline that combines robust data preprocessing, statistical exploratory data analysis, comparative regression and classification modeling, and an interactive risk categorization interface to provide an empirical, explainable, and proactive educational tool.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 7: 3. SYSTEM ANALYSIS AND DESIGN
    # =========================================================================
    add_sec_title("3. SYSTEM ANALYSIS AND DESIGN")

    add_p("The System Analysis and Design phase is an important step in the development of the Student Academic Performance Prediction System. It helps in understanding the problems in existing academic monitoring practices and designing an object-oriented, modular architecture that meets institutional counseling requirements while reinforcing core Machine Learning concepts.")

    add_sub_title("3.1 System Analysis")
    add_p("System analysis focuses on identifying the deficiencies in traditional student performance monitoring and defining the technical requirements for the predictive ML system.")

    add_p("Existing System: In many universities and colleges, academic evaluation is conducted reactively at the end of the term. Faculty mentors review student performance only after semester-end examination grades are published. When intermediate tracking exists, it relies on static heuristics—such as flagging students whose attendance drops below 75%—without considering study habits or continuous assignment quality.")

    add_p("Problems in the Existing System:")
    bullet_existing = [
        "● Delayed Intervention: Final exam failures are discovered after the semester has concluded, when remedial support is no longer possible.",
        "● Single-Metric Flaw: Rigid attendance thresholds fail to flag students who attend classes regularly but struggle severely with assignments or foundational concepts.",
        "● Subjective Evaluation: High student-to-mentor ratios make manual, individualized performance tracking slow, inconsistent, and error-prone.",
        "● Lack of Explainability: Traditional grading provides marks without identifying which specific behavioral levers (study hours, participation) would elevate performance."
    ]
    for b in bullet_existing:
        add_p(b, space_after=3)

    add_p("Proposed System: The proposed Student Academic Performance Prediction System is an interpretable Machine Learning pipeline built in Python. It ingests 10,000 multi-attribute student records, performs statistical imputation and scaling, forecasts continuous percentage scores via Multiple Linear Regression, classifies Pass/Fail status via Logistic Regression, and generates automated, four-tier academic counseling action plans.")

    add_p("Advantages of the Proposed System:")
    bullet_adv = [
        "● High Predictive Accuracy: Achieves 96.93% R² variance explanation (Random Forest), 96.63% R² (Linear Regression), and 96.60% Pass/Fail classification accuracy.",
        "● Automated Data Cleaning: Robust median imputation eliminates data loss from missing student logs.",
        "● Transparent Feature Weights: Explicitly quantifies the relative importance of prior marks, attendance, and study hours.",
        "● Actionable Counseling: Generates personalized academic prescriptions (Top Performer, Low Risk, Moderate Risk, High Risk) for every student."
    ]
    for b in bullet_adv:
        add_p(b, space_after=3)

    add_sub_title("3.2 System Design")
    add_p("System design describes how the application is structured across decoupled modules and how data flows through the preprocessing, training, and inference pipelines.")

    add_p("Modules of the System:")
    add_p("1. Data Ingestion & Loading Module (modules/data_loader.py): Safely reads student_data.csv and integrates automatic KaggleHub dataset fetching.")
    add_p("2. Data Preprocessing & Cleaning Module (modules/preprocessing.py): Imputes missing values, encodes binary categories, and fits StandardScaler.")
    add_p("3. Exploratory Data Analysis Module (modules/eda.py): Produces statistical distributions, Pearson correlation heatmaps, and regression plots.")
    add_p("4. Model Training & Evaluation Module (modules/models.py): Trains regression and classification models, extracts metrics, and serializes .pkl binaries.")
    add_p("5. Risk Advisory & Utilities Module (modules/utils.py): Performs input validation, multi-factor risk categorization, and custom QuickSort ranking.")
    add_p("6. Main CLI Execution Module (main.py): Orchestrates the pipeline and provides interactive student performance prediction.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 8: SYSTEM DESIGN CONTINUED & FIG 3.1
    # =========================================================================
    add_p("System Architecture: The system follows a layered architecture comprising the Presentation Layer (main.py CLI), Application/Module Layer (DataLoader, DataPreprocessor, ExploratoryDataAnalysis, ModelTrainer, and utils), Scientific Computing Core (NumPy, Pandas, Scikit-Learn), and Storage Layer (student_data.csv, .pkl binaries, and charts/ directory).")

    add_p("Technologies Used:")
    techs = [
        "● Programming Language: Python 3.14",
        "● Data Manipulation & Cleaning: Pandas 3.0.3, NumPy 2.x",
        "● Machine Learning Framework: Scikit-Learn (LinearRegression, Ridge, DecisionTree, RandomForest, LogisticRegression)",
        "● Data Visualization: Matplotlib 3.10, Seaborn 0.13",
        "● Model Serialization: Joblib (.pkl binaries)",
        "● Dataset Repository: Kaggle Hub (nikhil7280/student-performance-multiple-linear-regression)"
    ]
    for t in techs:
        add_p(t, space_after=3)

    add_p("", space_after=6)
    add_image_safe("charts/fig_3_1_data_flow.png", width_inches=6.2, caption="Fig. no. 3.1 – Module and data flow diagram")

    doc.add_page_break()

    # =========================================================================
    # PAGE 9: FIG 3.2 COMPONENT ARCHITECTURE
    # =========================================================================
    add_image_safe("charts/fig_3_2_system_architecture.png", width_inches=6.2, caption="Fig. no. 3.2 – Component architecture diagram")

    add_p("Overall, the system design ensures that the Student Academic Performance Prediction System is modular, computationally efficient, and highly interpretable. By separating data loading, preprocessing, model training, and user interaction into distinct classes, the codebase adheres to professional software engineering and machine learning design principles.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 10: 4. IMPLEMENTATION
    # =========================================================================
    add_sec_title("4. IMPLEMENTATION")

    add_p("The implementation phase involves translating the architectural design into robust, modular Python code. The project is organized within the MLPROJECT directory and structured into decoupled modules inside the modules/ package.")

    add_p("The Data Loader Module (modules/data_loader.py) defines the DataLoader class, which encapsulates safe file reading using try-except exception handling. If the dataset file is missing from the local directory, the module automatically invokes KaggleHub's dataset_download() API to retrieve the benchmark student performance dataset directly from Kaggle.")

    add_p("The Preprocessing Module (modules/preprocessing.py) implements the DataPreprocessor class. Real-world academic datasets frequently contain missing values due to administrative gaps. The clean_missing_values() method detects null entries across numerical attributes and performs median imputation (imputing 72.40% for missing attendance and 69.00% for missing marks). The encode_categorical() method maps binary text indicators (Internet_Access: Yes/No to 1/0). The feature matrix X is standardized using Scikit-Learn's StandardScaler, normalizing each feature to zero mean and unit variance according to the formula:")

    add_p("z = (x - μ) / σ", bold=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)

    add_p("The Exploratory Data Analysis Module (modules/eda.py) defines the ExploratoryDataAnalysis class. It executes automated visual inspection routines including score distribution histograms with KDE curves, Pass/Fail pie charts, Pearson correlation matrices, and study hours/attendance regression trendlines. All figures are generated in high-resolution (300 DPI) and exported to the charts/ directory.")

    add_p("The Model Training Module (modules/models.py) encapsulates the ModelTrainer class. The dataset is partitioned into an 80% training set and a 20% test set using train_test_split. Four regression algorithms (Linear Regression, Ridge Regression, Decision Tree Regressor, Random Forest Regressor) and two classification algorithms (Logistic Regression, Random Forest Classifier) are fitted on the scaled training features. Evaluation metrics including MAE, RMSE, R², Accuracy, Precision, Recall, and F1-score are computed on unseen test data, and the optimal models are saved as binary .pkl files using Joblib.")

    add_p("Input validation is implemented in modules/utils.py to ensure that user inputs entered through the CLI lie within valid academic and biological boundaries (e.g., attendance between 0–100%, study hours between 0–70 hours), handling invalid values gracefully without application crashes.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 11: FIG 4.1 DATA MODEL & IMPLEMENTATION SUMMARY
    # =========================================================================
    add_image_safe("charts/fig_4_1_data_model.png", width_inches=6.2, caption="Fig. 4.1 – Data model for student performance features, targets and risk tiers")

    add_p("Thus, the implementation phase transforms the system design into a fully functional Student Academic Performance Prediction System that reinforces object-oriented design, robust data preprocessing, statistical visualization, comparative machine learning evaluation, and real-time inference.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 12: 5. OUTPUT SCREENSHOTS (5.1 & 5.2)
    # =========================================================================
    add_sec_title("5. OUTPUT SCREENSHOT")

    add_p("The figures below display the actual output visualizations and screenshots captured from the executed Student Academic Performance Prediction System pipeline:")

    add_sub_title("5.1 :- Final Score Distribution and Pass/Fail Proportions")
    add_image_safe("charts/01_score_distribution.png", width_inches=6.0, caption="Fig. 5.1 – Student Final Score Distribution and Pass/Fail Proportion")

    add_sub_title("5.2 :- Feature Correlation Heatmap")
    add_image_safe("charts/02_correlation_heatmap.png", width_inches=4.8, caption="Fig. 5.2 – Pearson Correlation Matrix Heatmap across Numerical Features")

    doc.add_page_break()

    # =========================================================================
    # PAGE 13: 5. OUTPUT SCREENSHOTS (5.3 & 5.4)
    # =========================================================================
    add_sub_title("5.3 :- Study Hours per Week vs Final Score")
    add_image_safe("charts/03_study_vs_score.png", width_inches=5.2, caption="Fig. 5.3 – Study Hours per Week vs Final Score Scatter Trendline")

    add_sub_title("5.4 :- Attendance Percentage vs Final Score")
    add_image_safe("charts/04_attendance_vs_score.png", width_inches=5.2, caption="Fig. 5.4 – Attendance Percentage vs Final Score Scatter Plot")

    doc.add_page_break()

    # =========================================================================
    # PAGE 14: 5. OUTPUT SCREENSHOTS (5.5, 5.6 & 5.7)
    # =========================================================================
    add_sub_title("5.5 :- Actual vs Predicted Regression Fit")
    add_image_safe("charts/05_actual_vs_predicted.png", width_inches=5.2, caption="Fig. 5.5 – Actual vs Predicted Final Scores (Random Forest Regressor)")

    add_sub_title("5.6 :- Feature Importance Rankings")
    add_image_safe("charts/06_feature_importance.png", width_inches=5.2, caption="Fig. 5.6 – Relative Feature Importance Weights in Predicting Student Performance")

    doc.add_page_break()

    # =========================================================================
    # PAGE 14B: 5. OUTPUT SCREENSHOTS (5.7 & 5.8)
    # =========================================================================
    add_sub_title("5.7 :- Pass/Fail Classification Confusion Matrix")
    add_image_safe("charts/07_confusion_matrix.png", width_inches=4.6, caption="Fig. 5.7 – Confusion Matrix for Logistic Regression Pass/Fail Classification")

    add_sub_title("5.8 :- CLI Interactive Prediction Execution Output")
    add_image_safe("charts/08_cli_execution_output.png", width_inches=5.8, caption="Fig. 5.8 – Interactive Terminal Prediction and Academic Risk Advisory Execution")

    doc.add_page_break()

    # =========================================================================
    # PAGE 15: 6. SOURCE CODE (PART 1)
    # =========================================================================
    add_sec_title("6. SOURCE CODE")

    add_sub_title("6.1 :- modules/preprocessing.py (Data Cleaning, Imputation & Scaling)")
    code_prep = """
# modules/preprocessing.py
# Implements DataPreprocessor class: missing value imputation, encoding & scaling
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.feature_columns = None
        self.is_fitted = False

    def clean_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        df_clean = df.copy()
        for col in df_clean.columns:
            if df_clean[col].isnull().sum() > 0:
                if df_clean[col].dtype in ['float64', 'int64']:
                    median_val = df_clean[col].median()
                    df_clean[col] = df_clean[col].fillna(median_val)
                else:
                    mode_val = df_clean[col].mode()[0]
                    df_clean[col] = df_clean[col].fillna(mode_val)
        return df_clean

    def encode_categorical(self, df: pd.DataFrame) -> pd.DataFrame:
        df_encoded = df.copy()
        if 'Internet_Access' in df_encoded.columns:
            df_encoded['Internet_Access'] = df_encoded['Internet_Access'].map({'Yes': 1, 'No': 0})
        return df_encoded

    def prepare_features_and_targets(self, df: pd.DataFrame):
        df_clean = self.clean_missing_values(df)
        df_encoded = self.encode_categorical(df_clean)
        self.feature_columns = [
            'Attendance_Percentage', 'Study_Hours_Per_Week', 'Previous_Marks',
            'Assignment_Score', 'Class_Participation', 'Internet_Access'
        ]
        X = df_encoded[self.feature_columns]
        y_reg = df_encoded['Final_Score']
        y_clf = df_encoded['Pass_Fail'].map({'Pass': 1, 'Fail': 0})
        return X, y_reg, y_clf

    def fit_transform_scaling(self, X_train: pd.DataFrame) -> np.ndarray:
        X_scaled = self.scaler.fit_transform(X_train)
        self.is_fitted = True
        return X_scaled
"""
    add_code_block(doc, code_prep)

    add_sub_title("6.2 :- modules/models.py (Regression & Classification Pipelines)")
    code_models = """
# modules/models.py
# ModelTrainer class: trains, evaluates and persists ML models
from sklearn.linear_model import LinearRegression, Ridge, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, f1_score
import joblib, os

class ModelTrainer:
    def __init__(self, models_dir="models_saved"):
        self.models_dir = models_dir
        os.makedirs(self.models_dir, exist_ok=True)

    def train_and_evaluate_regression(self, X_train, X_test, y_train, y_test, feature_names):
        models = {
            "Linear Regression": LinearRegression(),
            "Ridge Regression": Ridge(alpha=1.0),
            "Decision Tree Regressor": DecisionTreeRegressor(max_depth=6, random_state=42),
            "Random Forest Regressor": RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42)
        }
        results = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            r2 = r2_score(y_test, y_pred)
            results[name] = {"MAE": mean_absolute_error(y_test, y_pred), "R2": r2}
        
        # Save best model
        best_model = models["Linear Regression"]
        joblib.dump(best_model, os.path.join(self.models_dir, "best_regression_model.pkl"))
        return results
"""
    add_code_block(doc, code_models)

    doc.add_page_break()

    # =========================================================================
    # PAGE 16: 6. SOURCE CODE (PART 2)
    # =========================================================================
    add_sub_title("6.3 :- modules/utils.py (Risk Categorization & Custom QuickSort)")
    code_utils = """
# modules/utils.py
# Risk categorization and custom manual QuickSort sorting algorithm
def categorize_risk_status(predicted_score: float, attendance: float, study_hours: float) -> dict:
    if predicted_score >= 80.0:
        grade = "A"
    elif predicted_score >= 70.0:
        grade = "B"
    elif predicted_score >= 60.0:
        grade = "C"
    elif predicted_score >= 50.0:
        grade = "D"
    else:
        grade = "F"
        
    if predicted_score < 50.0 or attendance < 60.0:
        risk_level = "HIGH RISK"
        plan = "Immediate academic intervention required. Mandatory remedial counseling."
    elif predicted_score < 65.0 or study_hours < 10.0:
        risk_level = "MODERATE RISK"
        plan = "Increase study hours to at least 15 hrs/week and focus on assignments."
    elif predicted_score < 80.0:
        risk_level = "LOW RISK"
        plan = "Good standing. Maintain study routine and aim for higher participation."
    else:
        risk_level = "TOP PERFORMER"
        plan = "Outstanding performance! Eligible for honors and peer-mentorship roles."
        
    return {"predicted_score": predicted_score, "grade": grade, "risk_level": risk_level, "action_plan": plan}

def custom_quick_sort(records: list, key_index: int = 1, reverse: bool = True) -> list:
    if len(records) <= 1:
        return records
    pivot = records[len(records) // 2]
    left = [x for x in records if (x[key_index] > pivot[key_index] if reverse else x[key_index] < pivot[key_index])]
    middle = [x for x in records if x[key_index] == pivot[key_index]]
    right = [x for x in records if (x[key_index] < pivot[key_index] if reverse else x[key_index] > pivot[key_index])]
    return custom_quick_sort(left, key_index, reverse) + middle + custom_quick_sort(right, key_index, reverse)
"""
    add_code_block(doc, code_utils)

    add_sub_title("6.4 :- main.py (Interactive Prediction CLI Execution Mode)")
    code_main = """
# main.py
# Interactive CLI prediction mode allowing real-time parameter inference
def interactive_prediction_mode():
    reg_path = os.path.join("models_saved", "best_regression_model.pkl")
    scaler_path = os.path.join("models_saved", "scaler.pkl")
    model = joblib.load(reg_path)
    scaler = joblib.load(scaler_path)
    
    print("Please enter student parameters:")
    att = float(input("1. Attendance Percentage (0 - 100%): "))
    study = float(input("2. Study Hours Per Week (0 - 70 hrs): "))
    prev = float(input("3. Previous Semester Marks (0 - 100%): "))
    assign = float(input("4. Assignment Score (0 - 100%): "))
    part = int(input("5. Class Participation Rating (1 - 10): "))
    internet_str = input("6. Has Home Internet Access? (Yes/No): ").strip().capitalize()
    
    is_valid, msg = validate_student_input(att, study, prev, assign, part)
    if not is_valid:
        print(f"[ERROR] {msg}"); return
        
    internet_num = 1 if internet_str == 'Yes' else 0
    input_df = pd.DataFrame([[att, study, prev, assign, part, internet_num]])
    input_scaled = scaler.transform(input_df)
    predicted_score = float(np.clip(model.predict(input_scaled)[0], 0.0, 100.0))
    risk_info = categorize_risk_status(predicted_score, att, study)
    print(f"Predicted Score: {predicted_score:.1f}% | Grade: {risk_info['grade']} | Risk: {risk_info['risk_level']}")
"""
    add_code_block(doc, code_main)

    doc.add_page_break()

    # =========================================================================
    # PAGE 17: 7. TESTING AND DEBUGGING
    # =========================================================================
    add_sec_title("7. TESTING AND DEBUGGING")

    add_sub_title("Introduction")
    add_p("Testing and debugging are critical phases in the development of the Student Academic Performance Prediction System. These processes verify that data ingestion executes reliably, that missing values are imputed accurately without data corruption, that feature scaling transforms numerical distributions correctly, and that machine learning models achieve the expected statistical generalization on unseen test data. Testing ensures that the analytical pipeline executes without failure, while debugging identifies and resolves logic and boundary edge-cases.")

    add_p("During development, distinct levels of testing were systematically conducted across all six system modules:")

    add_sub_title("Types of Testing")
    
    add_p("1. Unit Testing", bold=True, size=11, space_after=2)
    add_p("Unit testing involves testing individual functions, methods, and classes in isolation. For example, the clean_missing_values() method was tested on mock DataFrames containing simulated NaN entries to verify that median imputation is applied only to numeric columns, and the validate_student_input() function was tested across boundary limits (e.g., attendance < 0% or > 100%).")

    add_p("2. Integration Testing", bold=True, size=11, space_after=2)
    add_p("Integration testing validates seamless data interchange between interconnected modules. It verified that the DataFrame loaded by DataLoader is correctly ingested by DataPreprocessor, that the fitted StandardScaler is dumped and reloaded identically by main.py, and that predictions generated by ModelTrainer flow directly into categorize_risk_status() without type mismatches.")

    add_p("3. System Testing", bold=True, size=11, space_after=2)
    add_p("System testing verifies the complete end-to-end execution of the application as a unified pipeline. The run_training_pipeline() workflow was executed from a fresh terminal environment, verifying that data loading, preprocessing, EDA plot generation, multi-model evaluation, and model serialization complete automatically without runtime exceptions.")

    add_p("4. Model Validation & Performance Testing", bold=True, size=11, space_after=2)
    add_p("Model performance testing benchmarks machine learning metrics against strict quality standards. Regression performance was evaluated on unseen test data, achieving an R² of 96.93% and an RMSE of 3.371 with Random Forest Regressor (and R² = 96.63% with Linear Regression), verifying high predictive reliability without overfitting.")

    add_sub_title("Overall Conclusion")
    add_p("Through rigorous testing and systematic debugging, the Student Academic Performance Prediction System demonstrates robust stability, resilience against malformed inputs, and high predictive precision across all test scenarios.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 18: TEST CASES TABLE
    # =========================================================================
    add_sec_title("TEST CASES:--")

    tc_table = doc.add_table(rows=7, cols=6)
    tc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tc_table.autofit = False
    tc_widths = [Inches(0.8), Inches(1.3), Inches(1.3), Inches(1.5), Inches(0.9), Inches(0.7)]
    for row in tc_table.rows:
        for idx, width in enumerate(tc_widths):
            row.cells[idx].width = width

    tc_headers = ["Test Id", "Description", "Input", "Expected Result", "Actual Output", "Status"]
    for i, h in enumerate(tc_headers):
        cell = tc_table.cell(0, i)
        set_cell_background(cell, "E2E8F0")
        set_cell_margins(cell, top=100, bottom=100, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(9)

    test_rows = [
        ("TC-1", "Dataset Loading & Ingestion", "Call load_data() on student_data.csv", "Loads 10,000 records, 10 columns into DataFrame", "As expected", "Pass"),
        ("TC-2", "Missing Value Imputation", "DataFrame with ~2% nulls in Attendance/Marks", "Replaces NaN with column median (72.4% / 69.0%)", "As expected", "Pass"),
        ("TC-3", "Feature Matrix Standardization", "Scaled 6 feature columns via StandardScaler", "Outputs matrix with zero mean and unit variance", "As expected", "Pass"),
        ("TC-4", "High Performer Prediction", "Att: 92.5%, Study: 18h, Marks: 88%, Internet: Yes", "Score >= 80%, Grade A, TOP PERFORMER tier", "As expected", "Pass"),
        ("TC-5", "At-Risk Student Prediction", "Att: 48%, Study: 4h, Marks: 42%, Internet: No", "Score < 50%, Grade F, HIGH RISK intervention", "As expected", "Pass"),
        ("TC-6", "Boundary Range Validation", "Attendance = 150% (Invalid input)", "Handled gracefully via try-except, error shown", "As expected", "Pass")
    ]
    for r_idx, row_data in enumerate(test_rows, start=1):
        for c_idx, val in enumerate(row_data):
            cell = tc_table.cell(r_idx, c_idx)
            set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [0, 4, 5] else WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(val)
            run.font.size = Pt(8.5)
            if c_idx == 5:
                run.bold = True
                run.font.color.rgb = RGBColor(16, 185, 129)

    doc.add_page_break()

    # =========================================================================
    # PAGE 19: 8. CONCLUSION AND FUTURE ENHANCEMENT
    # =========================================================================
    add_sec_title("8. CONCLUSION AND FUTURE ENHANCEMENT")

    add_p("The Student Academic Performance Prediction System is designed to modernize and simplify academic progress monitoring by giving educators an automated, empirical, and interpretable Machine Learning pipeline. Traditional institutional evaluation systems often rely on post-semester exam results or rigid attendance heuristics, which can feel uninformative and too late for corrective guidance. This system provides an effective, data-driven solution built in Python that forecasts student performance reliably during the active semester.")

    add_p("The system enables faculty mentors to evaluate student potential across multiple academic and behavioral dimensions, compute expected percentage scores, and identify at-risk students before final exams. By using Python, NumPy, Pandas, Scikit-Learn, Matplotlib, and Seaborn, the system reinforces core concepts of object-oriented architecture, data cleaning, feature engineering, comparative regression, binary classification, model serialization, and custom QuickSort sorting algorithms.")

    add_p("Overall, the Student Academic Performance Prediction System improves the efficiency of academic counseling by providing high predictive precision (R² = 96.93%, Classification Accuracy = 96.60%), transparent feature rankings, and actionable remediation tiers for institutional mentors.")

    add_sub_title("Future Enhancement")
    add_p("Although the current system provides comprehensive capabilities for predictive modeling and risk profiling, several enhancements can be incorporated in future iterations to make the system more scalable and enterprise-ready:")

    enhancements = [
        ("1. Centralized Web Dashboard & Cloud Deployment", "Developing a web-based dashboard using Streamlit, FastAPI, or React to allow mentors and students to access prediction portals from browser and mobile interfaces."),
        ("2. Learning Management System (LMS) Integration", "Connecting directly to university LMS platforms (such as Moodle, Canvas, or Blackboard) via REST APIs to stream live attendance and assignment submissions automatically."),
        ("3. Longitudinal & Time-Series Deep Learning", "Integrating Recurrent Neural Networks (LSTMs or Transformers) to model semester-over-semester performance trajectories and track whether a student is improving or deteriorating over time."),
        ("4. Automated Real-Time Alerting System", "Integrating SMS and Email notification gateways to alert students and parents automatically when predicted scores trigger the Moderate or High Risk threshold."),
        ("5. Multi-Class Subject-Wise Breakdown", "Expanding the prediction engine from overall percentage forecasting to granular subject-specific predictions, identifying specific coursework modules where a student requires tutoring."),
        ("6. Mobile Application for Students and Parents", "Developing a cross-platform mobile application using Flutter or React Native to deliver personalized study recommendations directly to students' smartphones.")
    ]
    for h, desc in enhancements:
        add_p(f"{h}", bold=True, size=11, space_after=2)
        add_p(desc, size=10, space_after=8)

    add_p("With these future improvements, the Student Academic Performance Prediction System can evolve into a comprehensive, institution-wide Learning Analytics platform.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 20: 9. REFERENCES
    # =========================================================================
    add_sec_title("9. REFERENCES :--")

    refs = [
        ("Scikit-Learn – Official Documentation", "https://scikit-learn.org/stable/", "(For supervised regression, classification, StandardScaler, and model evaluation metrics)"),
        ("Pandas & NumPy Documentation", "https://pandas.pydata.org/  |  https://numpy.org/", "(For DataFrame manipulation, missing value median imputation, and numerical array operations)"),
        ("Matplotlib & Seaborn Documentation", "https://matplotlib.org/  |  https://seaborn.pydata.org/", "(For statistical data visualization, distribution histograms, correlation heatmaps, and regression plots)"),
        ("Kaggle Dataset Repository", "https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression", "(Student Performance Multiple Linear Regression benchmark dataset by Nikhil)"),
        ("Romero, C., & Ventura, S. (2020)", "Educational Data Mining and Learning Analytics: An updated survey. WIREs Data Mining and Knowledge Discovery, 10(3), e1355.", "(For literature foundations on predictive modeling in academic institutions)"),
        ("Cortez, P., & Silva, A. M. G. (2008)", "Using Data Mining to Predict Secondary School Student Performance. EUROSIS-ETI, pp. 5-12.", "(For empirical feature importance selection and regression analysis benchmarks)"),
        ("Python Software Foundation", "https://docs.python.org/3/", "(For Python 3.14 standard library, OOP specifications, and exception handling documentation)"),
        ("Class notes and study materials provided by Brainware University", "", "(Department of Computational Sciences, Bachelor of Computer Application curriculum)")
    ]

    for title, url, desc in refs:
        add_p(title, bold=True, size=11, space_after=1)
        if url:
            add_p(url, size=9.5, space_after=1, color=RGBColor(37, 99, 235))
        if desc:
            add_p(desc, italic=True, size=9.5, space_after=10, color=RGBColor(100, 116, 139))

    # Save Word document
    try:
        doc.save(output_path)
        print(f"[SUCCESS] Word Document generated: {output_path}")
    except PermissionError:
        alt_path = "Student_Performance_Prediction_Report_Updated.docx"
        doc.save(alt_path)
        print(f"[WARNING] '{output_path}' is currently locked (likely open in Word).")
        print(f"[SUCCESS] Saved synchronized report to: {alt_path}")
        output_path = alt_path
    return output_path

if __name__ == "__main__":
    build_word_document()
