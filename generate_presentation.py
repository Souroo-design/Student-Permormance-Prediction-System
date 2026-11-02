"""
Presentation Generator for Student Performance Prediction System
Generates an academic, 16:9 widescreen PowerPoint presentation (.pptx)
adhering to all 14 project component requirements.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_filename="Student_Performance_Prediction_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide layout

    # Color Palette Definitions
    COLOR_NAVY_DARK = RGBColor(15, 23, 42)      # #0F172A
    COLOR_NAVY_SLATE = RGBColor(30, 41, 59)     # #1E293B
    COLOR_PRIMARY_BLUE = RGBColor(37, 99, 235)  # #2563EB
    COLOR_ACCENT_CYAN = RGBColor(14, 165, 233)  # #0EA5E9
    COLOR_EMERALD = RGBColor(16, 185, 129)      # #10B981
    COLOR_AMBER = RGBColor(245, 158, 11)        # #F59E0B
    COLOR_ROSE = RGBColor(239, 68, 68)          # #EF4444
    COLOR_BG_LIGHT = RGBColor(248, 250, 252)    # #F8FAFC
    COLOR_CARD_BG = RGBColor(255, 255, 255)     # #FFFFFF
    COLOR_CARD_BORDER = RGBColor(226, 232, 240) # #E2E8F0
    COLOR_TEXT_MAIN = RGBColor(30, 41, 59)      # #1E293B
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B
    COLOR_WHITE = RGBColor(255, 255, 255)

    def add_header(slide, badge_text, title_text, category_num):
        """Adds standard clean header with badge pill, title, and slide category."""
        # Top banner background
        header_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        header_box.fill.solid()
        header_box.fill.fore_color.rgb = COLOR_CARD_BG
        header_box.line.color.rgb = COLOR_CARD_BORDER
        header_box.line.width = Pt(1)

        # Decorative left accent strip
        accent_strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.18), Inches(1.15))
        accent_strip.fill.solid()
        accent_strip.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
        accent_strip.line.fill.background()

        # Badge pill shape
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(0.18), Inches(2.3), Inches(0.3))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(239, 246, 255)
        pill.line.color.rgb = RGBColor(191, 219, 254)
        pill.line.width = Pt(0.75)
        tf_pill = pill.text_frame
        tf_pill.text = badge_text.upper()
        tf_pill.paragraphs[0].font.size = Pt(9.5)
        tf_pill.paragraphs[0].font.bold = True
        tf_pill.paragraphs[0].font.color.rgb = COLOR_PRIMARY_BLUE
        tf_pill.paragraphs[0].alignment = PP_ALIGN.CENTER

        # Title text
        title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.48), Inches(10.5), Inches(0.55))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = "Calibri"
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY_DARK

        # Category indicator on right
        num_box = slide.shapes.add_textbox(Inches(11.2), Inches(0.35), Inches(1.5), Inches(0.4))
        tf_num = num_box.text_frame
        p_num = tf_num.paragraphs[0]
        p_num.text = f"SECTION {category_num:02d}"
        p_num.font.size = Pt(11)
        p_num.font.bold = True
        p_num.font.color.rgb = COLOR_TEXT_MUTED
        p_num.alignment = PP_ALIGN.RIGHT

    def create_card(slide, left, top, width, height, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER):
        """Helper to create card container."""
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_NAVY_DARK
    bg1.line.fill.background()

    # Decorative background visual cards
    acc1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.2), Inches(-0.5), Inches(4.5), Inches(8.5))
    acc1.fill.solid()
    acc1.fill.fore_color.rgb = RGBColor(30, 41, 59)
    acc1.line.color.rgb = RGBColor(51, 65, 85)
    acc1.line.width = Pt(1)

    # Subject badge
    s1_pill = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.9), Inches(4.8), Inches(0.42))
    s1_pill.fill.solid()
    s1_pill.fill.fore_color.rgb = RGBColor(30, 58, 138)
    s1_pill.line.color.rgb = COLOR_PRIMARY_BLUE
    s1_pill.line.width = Pt(1)
    tf_s1 = s1_pill.text_frame
    p_s1 = tf_s1.paragraphs[0]
    p_s1.text = "PROBLEM BASED LEARNING (PBL)  •  MACHINE LEARNING"
    p_s1.font.size = Pt(11)
    p_s1.font.bold = True
    p_s1.font.color.rgb = RGBColor(147, 197, 253)
    p_s1.alignment = PP_ALIGN.CENTER

    # Project Title
    t_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(8.0), Inches(1.8))
    tf_t = t_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Student Academic Performance\nPrediction System"
    p_t.font.name = "Calibri"
    p_t.font.size = Pt(36)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_WHITE

    sub_box = slide1.shapes.add_textbox(Inches(1.0), Inches(3.4), Inches(8.0), Inches(0.8))
    tf_sub = sub_box.text_frame
    tf_sub.word_wrap = True
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "An Interpretable Multi-Algorithm Machine Learning Pipeline for Early Academic Risk Detection & Performance Forecasting"
    p_sub.font.size = Pt(14)
    p_sub.font.color.rgb = RGBColor(148, 163, 184)

    # Student & Project Metadata Cards
    # Left Box: Course Details
    c_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.5), Inches(3.8), Inches(2.2))
    c_box.fill.solid()
    c_box.fill.fore_color.rgb = RGBColor(30, 41, 59)
    c_box.line.color.rgb = RGBColor(51, 65, 85)
    tf_c = c_box.text_frame
    tf_c.word_wrap = True
    p = tf_c.paragraphs[0]
    p.text = "ACADEMIC & COURSE DETAILS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT_CYAN
    
    items_c = [
        ("Subject Name:", "Problem Based Learning (PBL) - ML"),
        ("Subject Code:", "[Enter Subject Code / e.g. CS501-PBL]"),
        ("Department:", "Computer Science & Engineering"),
        ("Development:", "Python 3.14 & Scikit-Learn in VS Code")
    ]
    for label, val in items_c:
        p2 = tf_c.add_paragraph()
        p2.text = f"{label} {val}"
        p2.font.size = Pt(10)
        p2.font.color.rgb = RGBColor(226, 232, 240)

    # Right Box: Student Details
    s_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.1), Inches(4.5), Inches(3.9), Inches(2.2))
    s_box.fill.solid()
    s_box.fill.fore_color.rgb = RGBColor(30, 41, 59)
    s_box.line.color.rgb = RGBColor(51, 65, 85)
    tf_s = s_box.text_frame
    tf_s.word_wrap = True
    p = tf_s.paragraphs[0]
    p.text = "STUDENT & PROJECT TEAM DETAILS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD

    items_s = [
        ("Student Name(s):", "[Student Name / Team Member Names]"),
        ("Roll Number(s):", "[Roll No. / University Seat Numbers]"),
        ("Batch / Section:", "[Batch 2023-2027 / Section A/B]"),
        ("Guide / Supervisor:", "[Faculty Mentor / Instructor Name]")
    ]
    for label, val in items_s:
        p2 = tf_s.add_paragraph()
        p2.text = f"{label} {val}"
        p2.font.size = Pt(10)
        p2.font.color.rgb = RGBColor(226, 232, 240)

    # Right side stat preview cards
    stats = [
        ("10,000", "Dataset Records", COLOR_PRIMARY_BLUE),
        ("96.93%", "R² Score (Best Model)", COLOR_EMERALD),
        ("96.60%", "Pass/Fail Accuracy", COLOR_ACCENT_CYAN)
    ]
    for i, (num, lbl, col) in enumerate(stats):
        stat_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.5), Inches(1.5 + i*1.7), Inches(3.2), Inches(1.35))
        stat_box.fill.solid()
        stat_box.fill.fore_color.rgb = RGBColor(15, 23, 42)
        stat_box.line.color.rgb = col
        stat_box.line.width = Pt(1.5)
        tf_stat = stat_box.text_frame
        tf_stat.word_wrap = True
        p1 = tf_stat.paragraphs[0]
        p1.text = num
        p1.font.size = Pt(24)
        p1.font.bold = True
        p1.font.color.rgb = col
        p1.alignment = PP_ALIGN.CENTER
        p2 = tf_stat.add_paragraph()
        p2.text = lbl
        p2.font.size = Pt(11)
        p2.font.color.rgb = RGBColor(148, 163, 184)
        p2.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 2: INTRODUCTION
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    slide2.background.fill.solid()
    slide2.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide2, "Introduction", "Background & Project Overview", 1)

    # 3 Column Cards
    intro_cards = [
        ("Academic Background", COLOR_PRIMARY_BLUE, [
            "In modern higher education, academic success depends on multifaceted factors rather than single exams.",
            "Key drivers include class attendance, consistent weekly study hours, assignment diligence, and active participation.",
            "Educational Data Mining (EDM) offers empirical methods to transform raw academic logs into predictive intelligence."
        ]),
        ("The Need for Early Detection", COLOR_AMBER, [
            "Traditional evaluation models identify failing students only post-semester exams when it is too late to intervene.",
            "Faculty members face high student-to-mentor ratios, making manual per-student tracking error-prone and subjective.",
            "Proactive identification enables structured mentoring, remedial sessions, and targeted academic counseling."
        ]),
        ("Project Solution Overview", COLOR_EMERALD, [
            "Builds a robust, production-grade Machine Learning pipeline in Python 3.14.",
            "Dual-target predictive intelligence: Continuous score regression (0-100%) and Pass/Fail classification.",
            "Includes an interactive CLI tool and automatic risk tier advisory with actionable academic prescriptions."
        ])
    ]

    for i, (title, color, bullets) in enumerate(intro_cards):
        card = create_card(slide2, 0.7 + i * 4.0, 1.45, 3.8, 5.4)
        
        # Top banner
        top_bar = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7 + i * 4.0), Inches(1.45), Inches(3.8), Inches(0.55))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = color
        top_bar.line.fill.background()
        tf_b = top_bar.text_frame
        p = tf_b.paragraphs[0]
        p.text = title.upper()
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

        # Content text
        c_box = slide2.shapes.add_textbox(Inches(0.85 + i * 4.0), Inches(2.2), Inches(3.5), Inches(4.4))
        tf = c_box.text_frame
        tf.word_wrap = True
        for b_idx, bullet in enumerate(bullets):
            p = tf.add_paragraph() if b_idx > 0 else tf.paragraphs[0]
            p.text = f"•  {bullet}"
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_TEXT_MAIN
            p.space_after = Pt(14)

    # =========================================================================
    # SLIDE 3: PROBLEM STATEMENT
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    slide3.background.fill.solid()
    slide3.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide3, "Problem Statement", "Defining the Core Real-World Challenge", 2)

    # Left: Big Callout Card for Core Problem Statement
    left_card = create_card(slide3, 0.7, 1.45, 6.2, 5.4)
    c_banner = slide3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.45), Inches(6.2), Inches(0.5))
    c_banner.fill.solid()
    c_banner.fill.fore_color.rgb = COLOR_ROSE
    c_banner.line.fill.background()
    p = c_banner.text_frame.paragraphs[0]
    p.text = "CORE PROBLEM FORMULATION"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    tb = slide3.shapes.add_textbox(Inches(0.95), Inches(2.15), Inches(5.7), Inches(4.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = '"How can educational institutions accurately predict final student academic performance and identify at-risk students early in the semester, using multi-factor academic and behavioral indicators, before final examinations occur?"'
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK
    p.space_after = Pt(14)

    bullet_pts = [
        "Delayed Academic Visibility: End-of-semester exams reveal failure after the term has already ended, making remediation impossible.",
        "Single-Metric Fallacy: Relying solely on attendance or midterm marks ignores critical multidimensional factors like study hours, assignment diligence, and participation.",
        "Manual Advisory Bottleneck: Mentors cannot manually compute risk scores for hundreds of students across diverse semesters.",
        "Need for Explainability: Black-box scores without factor importance fail to guide students on where they must improve."
    ]
    for b in bullet_pts:
        p2 = tf.add_paragraph()
        p2.text = f"• {b}"
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_after = Pt(8)

    # Right: 3 Impact / Consequence Cards
    impacts = [
        ("Student Attrition & Dropouts", COLOR_ROSE, "Without early intervention, high-risk students experience cumulative failure, leading to course repeats, lost credits, and increased dropout rates."),
        ("Inefficient Faculty Allocation", COLOR_AMBER, "Academic counseling resources are often deployed reactively rather than targeting the students who need urgent intervention most."),
        ("Institutional Accreditation Impact", COLOR_PRIMARY_BLUE, "Lower pass percentages and poor learning outcomes negatively impact NBA, NAAC, and institutional ranking metrics.")
    ]
    for i, (imp_title, imp_col, imp_desc) in enumerate(impacts):
        card = create_card(slide3, 7.2, 1.45 + i * 1.85, 5.4, 1.65)
        
        strip = slide3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.2), Inches(1.45 + i * 1.85), Inches(0.15), Inches(1.65))
        strip.fill.solid()
        strip.fill.fore_color.rgb = imp_col
        strip.line.fill.background()

        tb_imp = slide3.shapes.add_textbox(Inches(7.5), Inches(1.55 + i * 1.85), Inches(4.9), Inches(1.4))
        tf_imp = tb_imp.text_frame
        tf_imp.word_wrap = True
        p1 = tf_imp.paragraphs[0]
        p1.text = imp_title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = imp_col

        p2 = tf_imp.add_paragraph()
        p2.text = imp_desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = COLOR_TEXT_MAIN

    # =========================================================================
    # SLIDE 4: OBJECTIVES
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    slide4.background.fill.solid()
    slide4.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide4, "Objectives", "Project Aims & Expected Outcomes", 3)

    objectives = [
        ("1. Data Preprocessing & Cleaning", COLOR_PRIMARY_BLUE, [
            "Handle real-world data imperfections with missing value imputation (median for numerical values).",
            "Perform binary encoding on categorical features (e.g., Internet Access: Yes/No -> 1/0).",
            "Standardize features with StandardScaler (z-score normalization) to eliminate scale bias."
        ]),
        ("2. Exploratory Data Analysis (EDA)", COLOR_ACCENT_CYAN, [
            "Visualize statistical distributions of final scores, attendance, and study hours using Matplotlib & Seaborn.",
            "Generate correlation heatmaps to quantify multi-collinearity and feature-target relationships.",
            "Export high-resolution visualization figures (300 DPI) to charts/ directory for reporting."
        ]),
        ("3. Comparative Machine Learning", COLOR_EMERALD, [
            "Develop multiple regression models: Linear Regression, Ridge Regression, Decision Trees, and Random Forests.",
            "Evaluate regression performance with MAE, RMSE, and R² variance explained metrics.",
            "Implement classification models (Logistic Regression & Random Forest) for binary Pass/Fail prediction."
        ]),
        ("4. Explainability & Risk Advisory", COLOR_AMBER, [
            "Extract feature importance weights to reveal primary academic drivers.",
            "Design multi-factor risk categorization: Top Performer, Low Risk, Moderate Risk, High Risk.",
            "Generate tailored academic recommendations and intervention plans for mentors."
        ]),
        ("5. Python Syllabus Integration", RGBColor(147, 51, 234), [
            "Demonstrate core syllabus topics: OOP, Exception Handling, File I/O, Conditions, Loops, Collections.",
            "Implement a manual Custom QuickSort algorithm for score sorting without built-in functions.",
            "Build an interactive Command Line Interface (CLI) application in main.py for real-time predictions."
        ])
    ]

    for i, (obj_title, obj_color, obj_pts) in enumerate(objectives):
        col_idx = i % 2
        row_idx = i // 2
        if i == 4:
            # Full width bottom card for syllabus integration
            card = create_card(slide4, 0.7, 5.15, 11.9, 1.7)
            top_bar = slide4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(5.15), Inches(11.9), Inches(0.38))
            top_bar.fill.solid()
            top_bar.fill.fore_color.rgb = obj_color
            top_bar.line.fill.background()
            p = top_bar.text_frame.paragraphs[0]
            p.text = obj_title.upper()
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = COLOR_WHITE
            p.alignment = PP_ALIGN.LEFT

            tb = slide4.shapes.add_textbox(Inches(0.9), Inches(5.6), Inches(11.5), Inches(1.1))
            tf = tb.text_frame
            tf.word_wrap = True
            for pt_idx, pt in enumerate(obj_pts):
                p = tf.add_paragraph() if pt_idx > 0 else tf.paragraphs[0]
                p.text = f"• {pt}"
                p.font.size = Pt(10)
                p.font.color.rgb = COLOR_TEXT_MAIN
        else:
            w = 5.8
            h = 1.7
            left = 0.7 + col_idx * 6.1
            top = 1.45 + row_idx * 1.85
            card = create_card(slide4, left, top, w, h)
            
            top_bar = slide4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(w), Inches(0.38))
            top_bar.fill.solid()
            top_bar.fill.fore_color.rgb = obj_color
            top_bar.line.fill.background()
            p = top_bar.text_frame.paragraphs[0]
            p.text = obj_title.upper()
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = COLOR_WHITE

            tb = slide4.shapes.add_textbox(Inches(left + 0.15), Inches(top + 0.42), Inches(w - 0.3), Inches(h - 0.45))
            tf = tb.text_frame
            tf.word_wrap = True
            for pt_idx, pt in enumerate(obj_pts):
                p = tf.add_paragraph() if pt_idx > 0 else tf.paragraphs[0]
                p.text = f"• {pt}"
                p.font.size = Pt(9.5)
                p.font.color.rgb = COLOR_TEXT_MAIN

    # =========================================================================
    # SLIDE 5: SCOPE OF THE PROJECT
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    slide5.background.fill.solid()
    slide5.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide5, "Scope of the Project", "Coverage, Target Beneficiaries & Limitations", 4)

    # 3 Detailed Pillars
    pillars = [
        ("Project Coverage", COLOR_PRIMARY_BLUE, [
            ("Dataset Scale", "10,000 distinct student records downloaded from Kaggle Hub."),
            ("Feature Dimensions", "Key continuous and categorical predictors: Attendance %, Study Hours, Previous Marks, Assignment Scores, Class Participation, Home Internet."),
            ("Dual Prediction", "Simultaneous continuous Final Score % prediction and binary Pass/Fail classification."),
            ("Algorithm Breadth", "Covers Multiple Linear, Ridge, Decision Tree, Random Forest & Logistic Regression.")
        ]),
        ("Target Users", COLOR_EMERALD, [
            ("Faculty Advisors", "Identifies struggling students early to schedule one-on-one remedial sessions."),
            ("Department Heads", "Monitors aggregate course risk profiles and institutional pass percentage trends."),
            ("Students", "Provides transparent feedback on how improving study hours or attendance elevates predicted scores."),
            ("Counseling Units", "Directs mental and academic counseling resources toward high-risk students.")
        ]),
        ("System Limitations", COLOR_ROSE, [
            ("Qualitative Factors", "Does not capture personal health crises, financial stress, or extracurricular commitments."),
            ("Domain Boundary", "Trained on semester-level undergraduate academic data; requires fine-tuning for high school."),
            ("Static Model Baseline", "Batch-trained model requires periodic retraining with new semester cohort data."),
            ("Guidance Only", "Designed as an assistive decision-support tool, not for automated punitive decisions.")
        ])
    ]

    for i, (p_title, p_col, p_data) in enumerate(pillars):
        card = create_card(slide5, 0.7 + i * 4.0, 1.45, 3.8, 5.4)
        
        # Header bar
        hbar = slide5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7 + i * 4.0), Inches(1.45), Inches(3.8), Inches(0.55))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = p_col
        hbar.line.fill.background()
        p = hbar.text_frame.paragraphs[0]
        p.text = p_title.upper()
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

        tb = slide5.shapes.add_textbox(Inches(0.85 + i * 4.0), Inches(2.15), Inches(3.5), Inches(4.5))
        tf = tb.text_frame
        tf.word_wrap = True
        for b_idx, (subtitle, text) in enumerate(p_data):
            p = tf.add_paragraph() if b_idx > 0 else tf.paragraphs[0]
            p.text = f"{subtitle}: "
            p.font.bold = True
            p.font.size = Pt(10.5)
            p.font.color.rgb = p_col
            
            p2 = tf.add_paragraph()
            p2.text = text
            p2.font.size = Pt(9.5)
            p2.font.color.rgb = COLOR_TEXT_MAIN
            p2.space_after = Pt(10)

    # =========================================================================
    # SLIDE 6: LITERATURE REVIEW & EXISTING SYSTEM
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    slide6.background.fill.solid()
    slide6.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide6, "Literature Review", "Existing Systems & Research Gaps Identified", 5)

    # Left: Comparison Table of Existing vs Proposed
    # Existing System Analysis Card
    left_c = create_card(slide6, 0.7, 1.45, 5.8, 5.4)
    h_left = slide6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.45), Inches(5.8), Inches(0.5))
    h_left.fill.solid()
    h_left.fill.fore_color.rgb = COLOR_ROSE
    h_left.line.fill.background()
    p = h_left.text_frame.paragraphs[0]
    p.text = "EXISTING APPROACHES & LIMITATIONS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    tb_l = slide6.shapes.add_textbox(Inches(0.9), Inches(2.1), Inches(5.4), Inches(4.5))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    exist_points = [
        ("Traditional Cumulative Grading", "Evaluates performance strictly post-examination. Does not provide predictive foresight during active learning periods."),
        ("Static Attendance Threshold Rules", "Applies rigid cutoffs (e.g. attendance < 75%). Fails to capture students with 80% attendance who fail due to poor assignment scores or lack of study hours."),
        ("Isolated Midterm Scores", "Midterm marks alone explain only a fraction of total final variance; ignore continuous behavioral engagement."),
        ("No Automated Risk Categorization", "Lacks actionable remediation tiers; mentors must manually sift through hundreds of records without prioritized guidance.")
    ]
    for b_idx, (heading, desc) in enumerate(exist_points):
        p = tf_l.add_paragraph() if b_idx > 0 else tf_l.paragraphs[0]
        p.text = f"✖ {heading}"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_ROSE
        
        p2 = tf_l.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_after = Pt(10)

    # Right: Academic Literature Citations Card
    right_c = create_card(slide6, 6.8, 1.45, 5.8, 5.4)
    h_right = slide6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), Inches(1.45), Inches(5.8), Inches(0.5))
    h_right.fill.solid()
    h_right.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
    h_right.line.fill.background()
    p = h_right.text_frame.paragraphs[0]
    p.text = "INSIGHTS FROM ACADEMIC LITERATURE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    tb_r = slide6.shapes.add_textbox(Inches(7.0), Inches(2.1), Inches(5.4), Inches(4.5))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    lit_points = [
        ("Romero & Ventura (2020) - Educational Data Mining Survey", "Demonstrated that multi-variable regression models outperform single-attribute heuristics by over 40% in predicting student grade distributions."),
        ("Cortez & Silva (2008) - Predicting Student Performance", "Showed that combining prior academic records with real-time participation indicators provides optimal feature importance weights."),
        ("Linear Regression as an Interpretable Baseline", "Literature highlights that while deep neural networks offer accuracy, Multiple Linear Regression is vital in academic domains where explainability is required."),
        ("Our Research Contribution", "This project integrates high R² predictive regression (96.93% RF / 96.63% Linear) with syllabus-aligned Python modules and an instant interactive CLI advisory.")
    ]
    for b_idx, (heading, desc) in enumerate(lit_points):
        p = tf_r.add_paragraph() if b_idx > 0 else tf_r.paragraphs[0]
        p.text = f"✔ {heading}"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_BLUE
        
        p2 = tf_r.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_after = Pt(10)

    # =========================================================================
    # SLIDE 7: PROPOSED SYSTEM
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    slide7.background.fill.solid()
    slide7.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide7, "Proposed System", "Architecture of Proposed Machine Learning Solution", 6)

    props = [
        ("1. Automated Ingestion & Cleaning", COLOR_PRIMARY_BLUE, [
            "Seamless file loading via DataLoader class with exception handling.",
            "Automatic median imputation for missing marks or attendance entries.",
            "Binary categorical encoding for digital access features."
        ]),
        ("2. Dual Prediction Engine", COLOR_EMERALD, [
            "Continuous Regression: Predicts final percentage score with 96.93% R² accuracy.",
            "Binary Classification: Classifies Pass/Fail status with 96.60% accuracy.",
            "Model persistence via Joblib (.pkl) for instant inference."
        ]),
        ("3. Actionable Risk Advisory", COLOR_AMBER, [
            "Categorizes students into 4 distinct tiers: Top Performer, Low Risk, Moderate Risk, High Risk.",
            "Generates targeted academic action plans with personalized recommendations.",
            "Incorporates multi-factor conditions (study hours, attendance, predicted scores)."
        ]),
        ("4. Interactive CLI Interface", RGBColor(147, 51, 234), [
            "Simple terminal console for instructors to enter student parameters.",
            "Real-time validation against biological and academic boundaries.",
            "Demonstrates manual QuickSort algorithm for ranking students."
        ])
    ]

    for i, (title, col, pts) in enumerate(props):
        card = create_card(slide7, 0.7 + i * 2.95, 1.45, 2.8, 5.4)
        top_bar = slide7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7 + i * 2.95), Inches(1.45), Inches(2.8), Inches(0.55))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = col
        top_bar.line.fill.background()
        p = top_bar.text_frame.paragraphs[0]
        p.text = title.upper()
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

        tb = slide7.shapes.add_textbox(Inches(0.85 + i * 2.95), Inches(2.15), Inches(2.5), Inches(4.5))
        tf = tb.text_frame
        tf.word_wrap = True
        for b_idx, bullet in enumerate(pts):
            p = tf.add_paragraph() if b_idx > 0 else tf.paragraphs[0]
            p.text = f"• {bullet}"
            p.font.size = Pt(10)
            p.font.color.rgb = COLOR_TEXT_MAIN
            p.space_after = Pt(14)

    # =========================================================================
    # SLIDE 8: PROJECT METHODOLOGY
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    slide8.background.fill.solid()
    slide8.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide8, "Project Methodology", "Development Approach, Tools & Technology Stack", 7)

    # Left: Process Stages
    card_l = create_card(slide8, 0.7, 1.45, 6.2, 5.4)
    h_bar = slide8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.45), Inches(6.2), Inches(0.5))
    h_bar.fill.solid()
    h_bar.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
    h_bar.line.fill.background()
    p = h_bar.text_frame.paragraphs[0]
    p.text = "5-STAGE DEVELOPMENT METHODOLOGY (CRISP-DM)"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    stages = [
        ("Phase 1: Problem Definition & Data Sourcing", "10,000 student records fetched from KaggleHub API cache; standardized internal naming."),
        ("Phase 2: Preprocessing & Cleaning", "Imputed null values via median strategy; encoded binary attributes; scaled features via StandardScaler."),
        ("Phase 3: Exploratory Data Analysis (EDA)", "Formulated correlation matrix, distributions, and scatter trends; saved charts at 300 DPI."),
        ("Phase 4: ML Training & Model Selection", "80/20 train-test split; cross-evaluated Linear, Ridge, Decision Tree, and Random Forest models."),
        ("Phase 5: Deployment & CLI Integration", "Persisted optimal model binaries (.pkl); wrapped into interactive predictive CLI with validation.")
    ]
    tb = slide8.shapes.add_textbox(Inches(0.9), Inches(2.1), Inches(5.8), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    for idx, (stitle, sdesc) in enumerate(stages):
        p = tf.add_paragraph() if idx > 0 else tf.paragraphs[0]
        p.text = f"{stitle}"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_BLUE
        
        p2 = tf.add_paragraph()
        p2.text = sdesc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_after = Pt(8)

    # Right: Technology Stack Table / Badges
    card_r = create_card(slide8, 7.2, 1.45, 5.4, 5.4)
    h_bar_r = slide8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.2), Inches(1.45), Inches(5.4), Inches(0.5))
    h_bar_r.fill.solid()
    h_bar_r.fill.fore_color.rgb = COLOR_NAVY_SLATE
    h_bar_r.line.fill.background()
    p = h_bar_r.text_frame.paragraphs[0]
    p.text = "TECHNOLOGY STACK & TOOLS USED"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    tech_stack = [
        ("Programming Language", "Python 3.14 (Latest standard runtime)"),
        ("Development Environment", "Visual Studio Code (VS Code) on Windows"),
        ("Data Handling & Arrays", "Pandas 3.0.3, NumPy 2.x"),
        ("Machine Learning Library", "Scikit-Learn (LinearRegression, Ridge, Trees, Metrics)"),
        ("Data Visualization", "Matplotlib 3.10 & Seaborn 0.13 (Seaborn-v0_8 style)"),
        ("Model Persistence", "Joblib (Binary serialization .pkl)"),
        ("Dataset Repository", "KaggleHub (nikhil7280 Student Performance)")
    ]
    tb_t = slide8.shapes.add_textbox(Inches(7.4), Inches(2.1), Inches(5.0), Inches(4.5))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    for idx, (tname, tdesc) in enumerate(tech_stack):
        p = tf_t.add_paragraph() if idx > 0 else tf_t.paragraphs[0]
        p.text = f"• {tname}: "
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_BLUE
        
        run = p.add_run()
        run.text = tdesc
        run.font.bold = False
        run.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(9)

    # =========================================================================
    # SLIDE 9: PROJECT INTERNAL STRUCTURE
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    slide9.background.fill.solid()
    slide9.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide9, "Project Internal Structure", "System Architecture & Modular Decomposition", 8)

    modules_info = [
        ("modules/data_loader.py", COLOR_PRIMARY_BLUE, [
            "Class: DataLoader",
            "File handling with try-except blocks.",
            "Loads student_data.csv safely.",
            "Integrates KaggleHub dataset download fallback."
        ]),
        ("modules/preprocessing.py", COLOR_ACCENT_CYAN, [
            "Class: DataPreprocessor",
            "Handles median imputation for NaN values.",
            "Performs binary encoding (Internet_Access).",
            "Applies StandardScaler fit & transform.",
            "Bubble Sort demonstration implementation."
        ]),
        ("modules/eda.py", COLOR_EMERALD, [
            "Class: ExploratoryDataAnalysis",
            "Generates score distribution histograms & pie chart.",
            "Creates Pearson correlation matrix heatmap.",
            "Produces regression trendlines (Study & Attendance).",
            "Exports 300 DPI PNG visuals to charts/."
        ]),
        ("modules/models.py", COLOR_AMBER, [
            "Class: ModelTrainer",
            "Trains Linear Regression, Ridge, Decision Tree & RF.",
            "Computes MAE, RMSE, and R² scores.",
            "Trains Logistic Regression & RF Classifier.",
            "Extracts feature importances & confusion matrix."
        ]),
        ("modules/utils.py", RGBColor(147, 51, 234), [
            "Helper: categorize_risk_status()",
            "Multi-factor conditions (Score, Attendance, Study).",
            "Helper: validate_student_input()",
            "Manual QuickSort recursive implementation."
        ]),
        ("main.py (CLI Application)", COLOR_NAVY_DARK, [
            "Master pipeline orchestrator.",
            "Menu Option 1: Full pipeline execution.",
            "Menu Option 2: Interactive Student Predictor.",
            "Saves scaler.pkl and best_regression_model.pkl."
        ])
    ]

    for i, (m_name, m_col, m_pts) in enumerate(modules_info):
        col_idx = i % 3
        row_idx = i // 3
        left = 0.7 + col_idx * 4.0
        top = 1.45 + row_idx * 2.75
        card = create_card(slide9, left, top, 3.8, 2.6)

        bar = slide9.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(3.8), Inches(0.42))
        bar.fill.solid()
        bar.fill.fore_color.rgb = m_col
        bar.line.fill.background()
        p = bar.text_frame.paragraphs[0]
        p.text = m_name
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

        tb = slide9.shapes.add_textbox(Inches(left + 0.15), Inches(top + 0.5), Inches(3.5), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True
        for idx, pt in enumerate(m_pts):
            p = tf.add_paragraph() if idx > 0 else tf.paragraphs[0]
            p.text = f"• {pt}"
            p.font.size = Pt(9.5)
            p.font.color.rgb = COLOR_TEXT_MAIN
            p.space_after = Pt(4)

    # =========================================================================
    # SLIDE 10: IMPLEMENTATION - DATA PREPROCESSING & EDA
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    slide10.background.fill.solid()
    slide10.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide10, "Implementation: Part 1", "Data Cleaning, Preprocessing & Exploratory Data Analysis", 9)

    # Left: Explanation Card
    card_l10 = create_card(slide10, 0.7, 1.45, 5.0, 5.4)
    hbar_10 = slide10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.45), Inches(5.0), Inches(0.45))
    hbar_10.fill.solid()
    hbar_10.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
    hbar_10.line.fill.background()
    p = hbar_10.text_frame.paragraphs[0]
    p.text = "DATA PREPARATION & STATISTICAL INSIGHTS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    tb_10 = slide10.shapes.add_textbox(Inches(0.85), Inches(2.0), Inches(4.7), Inches(4.7))
    tf_10 = tb_10.text_frame
    tf_10.word_wrap = True

    prep_pts = [
        ("Missing Value Strategy", "Dataset includes intentional ~2% missing entries in Attendance and Previous Marks. Handled via median imputation (Attendance: 72.4%, Previous Marks: 69.0%) ensuring zero data loss."),
        ("Feature Standardization", "Applied Z-Score scaling: z = (x - μ) / σ using StandardScaler. Ensures features with large scales do not dominate model weights."),
        ("Score Distribution Insights", "Final scores range from 10% to 100% with a mean of 55.2%, forming a smooth distribution suitable for regression."),
        ("Correlation Findings", "Strongest positive correlations with Final Score: Previous Semester Marks (r = 0.92), Attendance Percentage (r = 0.76), and Study Hours per Week (r = 0.37).")
    ]
    for idx, (h, d) in enumerate(prep_pts):
        p = tf_10.add_paragraph() if idx > 0 else tf_10.paragraphs[0]
        p.text = f"✔ {h}"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_BLUE
        p2 = tf_10.add_paragraph()
        p2.text = d
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_after = Pt(8)

    # Right: Embed Real Chart Visuals
    # Chart 1: Distribution
    chart1_path = os.path.join("charts", "01_score_distribution.png")
    if os.path.exists(chart1_path):
        create_card(slide10, 5.9, 1.45, 6.7, 2.6)
        slide10.shapes.add_picture(chart1_path, Inches(6.0), Inches(1.5), Inches(6.5), Inches(2.5))
    
    # Chart 2: Correlation Heatmap
    chart2_path = os.path.join("charts", "02_correlation_heatmap.png")
    if os.path.exists(chart2_path):
        create_card(slide10, 5.9, 4.2, 6.7, 2.65)
        slide10.shapes.add_picture(chart2_path, Inches(7.4), Inches(4.25), Inches(3.7), Inches(2.55))

    # =========================================================================
    # SLIDE 11: IMPLEMENTATION - MODEL TRAINING & FEATURE IMPORTANCE
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    slide11.background.fill.solid()
    slide11.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide11, "Implementation: Part 2", "Model Training, Regression Fit & Feature Importance", 10)

    # Left: Explanation Card
    card_l11 = create_card(slide11, 0.7, 1.45, 5.0, 5.4)
    hbar_11 = slide11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.45), Inches(5.0), Inches(0.45))
    hbar_11.fill.solid()
    hbar_11.fill.fore_color.rgb = COLOR_EMERALD
    hbar_11.line.fill.background()
    p = hbar_11.text_frame.paragraphs[0]
    p.text = "MODEL FITTING & FEATURE RANKINGS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    tb_11 = slide11.shapes.add_textbox(Inches(0.85), Inches(2.0), Inches(4.7), Inches(4.7))
    tf_11 = tb_11.text_frame
    tf_11.word_wrap = True

    model_pts = [
        ("Multiple Linear Regression & Random Forest", "Trained on scaled feature matrix. Evaluated across 4 regression algorithms, achieving exceptional predictive accuracy along the 45-degree diagonal line."),
        ("R² Goodness of Fit", "Random Forest Regressor achieved R² = 96.93% (MAE = 2.18%) and Multiple Linear Regression achieved R² = 96.63% (MAE = 2.09%), explaining ~97% of total student performance variance."),
        ("Feature Importance Extraction", "Ensemble Gini importance and standardized regression weights reveal the top predictive drivers of student grades."),
        ("Primary Drivers of Success", "1. Previous Marks (85.1% weight)\n2. Study Hours / Week (14.3% weight)\n3. Attendance Percentage (0.5% weight)\n4. Assignment Score & Participation (0.1% weight)")
    ]
    for idx, (h, d) in enumerate(model_pts):
        p = tf_11.add_paragraph() if idx > 0 else tf_11.paragraphs[0]
        p.text = f"✔ {h}"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_EMERALD
        p2 = tf_11.add_paragraph()
        p2.text = d
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_after = Pt(8)

    # Right: Embed Real Chart Visuals
    # Chart 5: Actual vs Predicted
    chart5_path = os.path.join("charts", "05_actual_vs_predicted.png")
    if os.path.exists(chart5_path):
        create_card(slide11, 5.9, 1.45, 6.7, 2.6)
        slide11.shapes.add_picture(chart5_path, Inches(6.1), Inches(1.5), Inches(6.3), Inches(2.5))
    
    # Chart 6: Feature Importance
    chart6_path = os.path.join("charts", "06_feature_importance.png")
    if os.path.exists(chart6_path):
        create_card(slide11, 5.9, 4.2, 6.7, 2.65)
        slide11.shapes.add_picture(chart6_path, Inches(6.1), Inches(4.25), Inches(6.3), Inches(2.55))

    # =========================================================================
    # SLIDE 12: TESTING AND RESULTS
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    slide12.background.fill.solid()
    slide12.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide12, "Testing and Results", "Experimental Evaluation, Test Cases & Metrics", 11)

    # Left: Regression & Classification Comparative Tables
    card_l12 = create_card(slide12, 0.7, 1.45, 6.6, 5.4)
    hbar_12 = slide12.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.45), Inches(6.6), Inches(0.45))
    hbar_12.fill.solid()
    hbar_12.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
    hbar_12.line.fill.background()
    p = hbar_12.text_frame.paragraphs[0]
    p.text = "MODEL PERFORMANCE METRICS & VALIDATION RESULTS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    # Table 1: Regression
    tb_title1 = slide12.shapes.add_textbox(Inches(0.9), Inches(1.95), Inches(6.2), Inches(0.3))
    p = tb_title1.text_frame.paragraphs[0]
    p.text = "Regression Model Comparison (Predicting Final Score %)"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_BLUE

    # Add PPTX Table for Regression
    rows = 5
    cols = 4
    left = Inches(0.9)
    top = Inches(2.3)
    width = Inches(6.2)
    height = Inches(1.4)
    table_shape = slide12.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    table_data = [
        ["Model Algorithm", "MAE", "RMSE", "R² Score"],
        ["Random Forest Regressor (Best)", "2.177", "3.371", "96.93%"],
        ["Linear Regression", "2.094", "3.535", "96.63%"],
        ["Ridge Regression", "2.094", "3.535", "96.63%"],
        ["Decision Tree Regressor", "2.871", "4.125", "95.41%"]
    ]
    for r_idx, row in enumerate(table_data):
        for c_idx, cell_text in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = cell_text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(9)
            if r_idx == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_WHITE
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_NAVY_DARK
            elif r_idx == 1:
                p.font.bold = True
                p.font.color.rgb = COLOR_PRIMARY_BLUE
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(239, 246, 255)
            else:
                p.font.color.rgb = COLOR_TEXT_MAIN
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_WHITE

    # Test cases below table
    tb_tc = slide12.shapes.add_textbox(Inches(0.9), Inches(3.85), Inches(6.2), Inches(2.9))
    tf_tc = tb_tc.text_frame
    tf_tc.word_wrap = True
    p = tf_tc.paragraphs[0]
    p.text = "Unit & Integration Test Cases Executed:"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK

    test_cases = [
        ("Test Case 1 (High Performer)", "Input: Attendance 92.5%, Study 18h, Marks 88%, Internet Yes -> Result: Predicted 85.8%, Grade A, TOP PERFORMER (Passed)."),
        ("Test Case 2 (At-Risk Student)", "Input: Attendance 48%, Study 4h, Marks 42%, Internet No -> Result: Predicted 23.9%, Grade F, HIGH RISK (Passed)."),
        ("Test Case 3 (Boundary Validation)", "Input: Attendance 150% (Invalid) -> Result: Graceful error handled via try-except boundary validation (Passed).")
    ]
    for idx, (tc_title, tc_res) in enumerate(test_cases):
        p = tf_tc.add_paragraph()
        p.text = f"• {tc_title}: "
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_EMERALD if "Passed" in tc_res else COLOR_ROSE
        run = p.add_run()
        run.text = tc_res
        run.font.bold = False
        run.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(4)

    # Right: Classification Confusion Matrix Picture
    card_r12 = create_card(slide12, 7.5, 1.45, 5.1, 5.4)
    hbar_r12 = slide12.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.5), Inches(1.45), Inches(5.1), Inches(0.45))
    hbar_r12.fill.solid()
    hbar_r12.fill.fore_color.rgb = COLOR_EMERALD
    hbar_r12.line.fill.background()
    p = hbar_r12.text_frame.paragraphs[0]
    p.text = "CLASSIFICATION METRICS (PASS/FAIL)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    chart7_path = os.path.join("charts", "07_confusion_matrix.png")
    if os.path.exists(chart7_path):
        slide12.shapes.add_picture(chart7_path, Inches(7.7), Inches(2.0), Inches(4.7), Inches(3.4))

    # Metric summaries below confusion matrix
    tb_m = slide12.shapes.add_textbox(Inches(7.7), Inches(5.5), Inches(4.7), Inches(1.2))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True
    p = tf_m.paragraphs[0]
    p.text = "Logistic Regression Classification Results:"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_DARK

    p2 = tf_m.add_paragraph()
    p2.text = "• Accuracy: 96.60%  |  Precision: 0.967\n• Recall: 0.975      |  F1-Score: 0.971 (Weighted)"
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = COLOR_TEXT_MAIN

    # =========================================================================
    # SLIDE 13: CONCLUSION
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    slide13.background.fill.solid()
    slide13.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide13, "Conclusion", "Project Summary & Objectives Fulfillment", 12)

    conclusions = [
        ("High Predictive Accuracy", COLOR_PRIMARY_BLUE, "Successfully engineered predictive regression models achieving R² = 96.93% (Random Forest) and 96.63% (Multiple Linear Regression), with MAE ~ 2.09–2.18%, demonstrating that student academic performance can be reliably modeled before final exams."),
        ("Multi-Tier Risk Detection", COLOR_EMERALD, "Transitioned educational decision-making from reactive grading to early intervention. Implemented automated 4-tier risk categorization with personalized counseling action plans."),
        ("Transparent Explainability", COLOR_ACCENT_CYAN, "Identified Prior Semester Marks (85.1%) and Study Hours per Week (14.3%) as the primary determinants of academic standing, guiding students on where to focus."),
        ("Syllabus & Engineering Alignment", RGBColor(147, 51, 234), "Integrated all core Python curriculum concepts: OOP, File Handling, Exception Handling, Custom QuickSort sorting algorithm, NumPy, Pandas, and Scikit-Learn into a functional CLI tool.")
    ]

    for i, (ctitle, ccol, cdesc) in enumerate(conclusions):
        card = create_card(slide13, 0.7 + i * 2.95, 1.45, 2.8, 5.4)
        top_bar = slide13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7 + i * 2.95), Inches(1.45), Inches(2.8), Inches(0.55))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = ccol
        top_bar.line.fill.background()
        p = top_bar.text_frame.paragraphs[0]
        p.text = ctitle.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

        tb = slide13.shapes.add_textbox(Inches(0.85 + i * 2.95), Inches(2.2), Inches(2.5), Inches(4.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = cdesc
        p.font.size = Pt(10.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 14: FUTURE SCOPE
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    slide14.background.fill.solid()
    slide14.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide14, "Future Scope", "Potential Extensions & System Roadmap", 13)

    future_pts = [
        ("Web Dashboard & Cloud Deployment", COLOR_PRIMARY_BLUE, [
            "Develop an interactive web portal using FastAPI / Streamlit or React.",
            "Allow faculty and students to access prediction portals from mobile devices.",
            "Host on institutional cloud infrastructure with role-based access control."
        ]),
        ("LMS / ERP Integration", COLOR_EMERALD, [
            "Connect directly to university Learning Management Systems (Moodle, Canvas, Google Classroom).",
            "Automatically stream live attendance and assignment submissions via REST APIs.",
            "Eliminate manual CSV data entry."
        ]),
        ("Longitudinal & Deep Learning Models", COLOR_ACCENT_CYAN, [
            "Incorporate Recurrent Neural Networks (LSTMs or Transformers) to capture temporal progress trends over multiple semesters.",
            "Analyze trajectory: whether a student's performance is improving or declining over time."
        ]),
        ("Automated Multi-Channel Alerting", COLOR_AMBER, [
            "Send automated, personalized SMS / Email notifications to students entering moderate or high risk.",
            "Schedule automatic counseling appointments with assigned faculty mentors."
        ])
    ]

    for i, (ftitle, fcol, fitems) in enumerate(future_pts):
        card = create_card(slide14, 0.7 + i * 2.95, 1.45, 2.8, 5.4)
        top_bar = slide14.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7 + i * 2.95), Inches(1.45), Inches(2.8), Inches(0.55))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = fcol
        top_bar.line.fill.background()
        p = top_bar.text_frame.paragraphs[0]
        p.text = ftitle.upper()
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

        tb = slide14.shapes.add_textbox(Inches(0.85 + i * 2.95), Inches(2.15), Inches(2.5), Inches(4.5))
        tf = tb.text_frame
        tf.word_wrap = True
        for b_idx, bullet in enumerate(fitems):
            p = tf.add_paragraph() if b_idx > 0 else tf.paragraphs[0]
            p.text = f"• {bullet}"
            p.font.size = Pt(10)
            p.font.color.rgb = COLOR_TEXT_MAIN
            p.space_after = Pt(14)

    # =========================================================================
    # SLIDE 15: REFERENCES
    # =========================================================================
    slide15 = prs.slides.add_slide(blank_layout)
    slide15.background.fill.solid()
    slide15.background.fill.fore_color.rgb = COLOR_BG_LIGHT
    add_header(slide15, "References", "Literature Citations, Documentation & Sources", 14)

    # 2 Column Reference Cards
    ref_left = create_card(slide15, 0.7, 1.45, 5.8, 5.4)
    h_rl = slide15.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.45), Inches(5.8), Inches(0.45))
    h_rl.fill.solid()
    h_rl.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
    h_rl.line.fill.background()
    p = h_rl.text_frame.paragraphs[0]
    p.text = "ACADEMIC PAPERS & BOOKS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    tb_rl = slide15.shapes.add_textbox(Inches(0.9), Inches(2.05), Inches(5.4), Inches(4.6))
    tf_rl = tb_rl.text_frame
    tf_rl.word_wrap = True

    academic_refs = [
        ("Romero, C., & Ventura, S. (2020)", "Educational Data Mining and Learning Analytics: An updated survey. WIREs Data Mining and Knowledge Discovery, 10(3), e1355."),
        ("Cortez, P., & Silva, A. M. G. (2008)", "Using Data Mining to Predict Secondary School Student Performance. Proceedings of 5th Annual Future Business Technology Conference, Porto, Portugal."),
        ("James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021)", "An Introduction to Statistical Learning: with Applications in Python. Springer Texts in Statistics."),
        ("Baker, R. S., & Inventado, P. S. (2014)", "Educational Data Mining and Learning Analytics. In Learning Analytics (pp. 61-75). Springer, New York, NY.")
    ]
    for idx, (auth, title) in enumerate(academic_refs):
        p = tf_rl.add_paragraph() if idx > 0 else tf_rl.paragraphs[0]
        p.text = f"[{idx+1}] {auth}"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_BLUE
        
        p2 = tf_rl.add_paragraph()
        p2.text = title
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_after = Pt(10)

    ref_right = create_card(slide15, 6.8, 1.45, 5.8, 5.4)
    h_rr = slide15.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), Inches(1.45), Inches(5.8), Inches(0.45))
    h_rr.fill.solid()
    h_rr.fill.fore_color.rgb = COLOR_NAVY_SLATE
    h_rr.line.fill.background()
    p = h_rr.text_frame.paragraphs[0]
    p.text = "OFFICIAL DOCUMENTATION & DATA REPOSITORIES"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    tb_rr = slide15.shapes.add_textbox(Inches(7.0), Inches(2.05), Inches(5.4), Inches(4.6))
    tf_rr = tb_rr.text_frame
    tf_rr.word_wrap = True

    web_refs = [
        ("Scikit-Learn Documentation", "Machine Learning in Python - Supervised Learning & Model Evaluation Metrics (https://scikit-learn.org/stable/)."),
        ("Pandas & NumPy Documentation", "DataFrame Operations, Data Cleaning, and High-Performance Array Computations (https://pandas.pydata.org/)."),
        ("Kaggle Dataset Repository", "Student Performance Multiple Linear Regression Dataset by Nikhil (https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression)."),
        ("Python Software Foundation", "Python 3.14 Official Language Reference & Standard Library (https://docs.python.org/3/).")
    ]
    for idx, (auth, title) in enumerate(web_refs):
        p = tf_rr.add_paragraph() if idx > 0 else tf_rr.paragraphs[0]
        p.text = f"[{idx+5}] {auth}"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY_SLATE
        
        p2 = tf_rr.add_paragraph()
        p2.text = title
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_after = Pt(10)

    # =========================================================================
    # SLIDE 16: THANK YOU / Q&A SLIDE
    # =========================================================================
    slide16 = prs.slides.add_slide(blank_layout)
    bg16 = slide16.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg16.fill.solid()
    bg16.fill.fore_color.rgb = COLOR_NAVY_DARK
    bg16.line.fill.background()

    # Center card
    card_ty = slide16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.6), Inches(1.5), Inches(8.1), Inches(4.5))
    card_ty.fill.solid()
    card_ty.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card_ty.line.color.rgb = COLOR_PRIMARY_BLUE
    card_ty.line.width = Pt(1.5)

    tb_ty = slide16.shapes.add_textbox(Inches(2.8), Inches(1.9), Inches(7.7), Inches(3.7))
    tf_ty = tb_ty.text_frame
    tf_ty.word_wrap = True

    p = tf_ty.paragraphs[0]
    p.text = "THANK YOU!"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    p2 = tf_ty.add_paragraph()
    p2.text = "Questions & Answers / Viva Voce Discussion"
    p2.font.size = Pt(18)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_ACCENT_CYAN
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(8)
    p2.space_after = Pt(20)

    p3 = tf_ty.add_paragraph()
    p3.text = "Student Academic Performance Prediction System\nPBL - Machine Learning  •  Department of Computer Science & Engineering"
    p3.font.size = Pt(12)
    p3.font.color.rgb = RGBColor(203, 213, 225)
    p3.alignment = PP_ALIGN.CENTER

    p4 = tf_ty.add_paragraph()
    p4.text = "Project Codebase, Charts & Models available in MLPROJECT directory."
    p4.font.size = Pt(10.5)
    p4.font.italic = True
    p4.font.color.rgb = RGBColor(148, 163, 184)
    p4.alignment = PP_ALIGN.CENTER
    p4.space_before = Pt(15)

    # Save presentation
    candidates = [
        output_filename,
        "Student_Performance_Prediction_Presentation_Updated.pptx",
        "Student_Performance_Prediction_Presentation_Final.pptx",
        "Student_Performance_Prediction_Presentation_Corrected.pptx"
    ]
    saved_path = None
    for cand in candidates:
        try:
            prs.save(cand)
            saved_path = cand
            print(f"[SUCCESS] Presentation generated successfully: {cand}")
            break
        except PermissionError:
            continue

    if not saved_path:
        import time
        ts = int(time.time())
        cand = f"Student_Performance_Prediction_Presentation_{ts}.pptx"
        prs.save(cand)
        saved_path = cand
        print(f"[SUCCESS] Saved to timestamped file: {cand}")

    return saved_path

if __name__ == "__main__":
    create_deck()
