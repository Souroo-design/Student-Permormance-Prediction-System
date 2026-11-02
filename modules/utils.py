"""
Utilities Module - Demonstrates Python Syllabus Concepts:
Conditions, Loops, Collections, Manual Sorting, and Exception Handling.
"""

import sys

def categorize_risk_status(predicted_score: float, attendance: float, study_hours: float) -> dict:
    """
    Demonstrates Syllabus Topic: Conditions (if-elif-else).
    Categorizes student risk level and provides academic recommendations based on multi-factor rules.
    """
    # 1. Determine Grade
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
        
    # 2. Multi-factor Condition for Risk Level
    if predicted_score < 50.0 or attendance < 60.0:
        risk_level = "HIGH RISK"
        color_code = "\033[91m" # Red
        action_plan = "Immediate academic intervention required. Mandatory remedial classes and counseling recommended."
    elif predicted_score < 65.0 or study_hours < 10.0:
        risk_level = "MODERATE RISK"
        color_code = "\033[93m" # Yellow
        action_plan = "Increase study hours to at least 15 hours/week and focus on weekly assignment completion."
    elif predicted_score < 80.0:
        risk_level = "LOW RISK"
        color_code = "\033[92m" # Green
        action_plan = "Good academic standing. Maintain current study routine and aim for higher class participation."
    else:
        risk_level = "TOP PERFORMER"
        color_code = "\033[96m" # Cyan
        action_plan = "Excellent performance! Eligible for academic honors and advanced peer-mentorship roles."
        
    return {
        "predicted_score": predicted_score,
        "grade": grade,
        "pass_fail": "Pass" if predicted_score >= 50.0 else "Fail",
        "risk_level": risk_level,
        "action_plan": action_plan
    }


def validate_student_input(attendance: float, study_hours: float, prev_marks: float, assign_score: float, participation: int) -> tuple:
    """
    Demonstrates Syllabus Topic: Exception Handling and Validation.
    Validates numeric range boundaries for user inputs.
    """
    try:
        attendance = float(attendance)
        study_hours = float(study_hours)
        prev_marks = float(prev_marks)
        assign_score = float(assign_score)
        participation = int(participation)
        
        # Range checks using loops and conditions
        validations = [
            ("Attendance", attendance, 0.0, 100.0),
            ("Study Hours", study_hours, 0.0, 70.0),
            ("Previous Marks", prev_marks, 0.0, 100.0),
            ("Assignment Score", assign_score, 0.0, 100.0),
            ("Participation Rating", participation, 1, 10)
        ]
        
        for name, val, min_val, max_val in validations:
            if not (min_val <= val <= max_val):
                raise ValueError(f"Input '{name}' value {val} is outside allowed range [{min_val}, {max_val}].")
                
        return True, "Valid inputs"
        
    except ValueError as val_err:
        return False, str(val_err)
    except Exception as err:
        return False, f"Unexpected error during validation: {err}"


def custom_quick_sort(records: list, key_index: int = 1, reverse: bool = True) -> list:
    """
    Demonstrates Syllabus Topic: Manual Sorting Algorithm (QuickSort implementation).
    Recursively sorts a list of tuples/dictionaries by given key index without using builtin sort().
    """
    if len(records) <= 1:
        return records
    
    pivot = records[len(records) // 2]
    pivot_val = pivot[key_index] if isinstance(pivot, (list, tuple)) else pivot[key_index]
    
    if reverse:
        left = [x for x in records if (x[key_index] if isinstance(x, (list, tuple)) else x[key_index]) > pivot_val]
        middle = [x for x in records if (x[key_index] if isinstance(x, (list, tuple)) else x[key_index]) == pivot_val]
        right = [x for x in records if (x[key_index] if isinstance(x, (list, tuple)) else x[key_index]) < pivot_val]
    else:
        left = [x for x in records if (x[key_index] if isinstance(x, (list, tuple)) else x[key_index]) < pivot_val]
        middle = [x for x in records if (x[key_index] if isinstance(x, (list, tuple)) else x[key_index]) == pivot_val]
        right = [x for x in records if (x[key_index] if isinstance(x, (list, tuple)) else x[key_index]) > pivot_val]
        
    return custom_quick_sort(left, key_index, reverse) + middle + custom_quick_sort(right, key_index, reverse)


if __name__ == "__main__":
    # Test quick sort
    data = [("Alice", 78.5), ("Bob", 92.0), ("Charlie", 45.0), ("David", 88.0)]
    sorted_data = custom_quick_sort(data, key_index=1, reverse=True)
    print("QuickSort Result (Descending):", sorted_data)
