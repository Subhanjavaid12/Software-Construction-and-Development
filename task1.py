"""
student_result.py
Guided Lab: Refactored Student Result Program with cohesive functions.
"""

from typing import List, Dict, Any


# --- CALCULATION LOGIC ---

def calculate_total(marks: List[float]) -> float:
    """Calculates and returns the sum of student marks."""
    return sum(marks)


def calculate_percentage(total_marks: float, max_marks: float) -> float:
    """Calculates the percentage based on total and maximum marks possible."""
    if max_marks <= 0:
        raise ValueError("Maximum marks must be greater than zero.")
    return (total_marks / max_marks) * 100.0


# --- DECISION LOGIC ---

def determine_grade(percentage: float) -> str:
    """Determines the letter grade according to the score percentage."""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def is_passing(percentage: float, passing_threshold: float = 50.0) -> bool:
    """Checks whether the student meets the passing threshold."""
    return percentage >= passing_threshold


# --- PRESENTATION / OUTPUT LOGIC ---

def format_student_report(name: str, total: float, percentage: float, grade: str, passed: bool) -> str:
    """Formats the calculated student results into a clean text report."""
    status = "PASSED" if passed else "FAILED"
    return (
        f"----------------------------------------\n"
        f"Student Name : {name}\n"
        f"Total Score  : {total:.2f}\n"
        f"Percentage   : {percentage:.2f}%\n"
        f"Grade        : {grade}\n"
        f"Status       : {status}\n"
        f"----------------------------------------"
    )


def display_report(report_text: str) -> None:
    """Handles output display."""
    print(report_text)


# --- COORDINATOR / ORCHESTRATION ---

def process_student(name: str, marks: List[float], max_marks: float) -> None:
    """
    Coordinates calculation, evaluation, and reporting 
    without holding implementation details directly.
    """
    total = calculate_total(marks)
    percentage = calculate_percentage(total, max_marks)
    grade = determine_grade(percentage)
    passed = is_passing(percentage)

    report = format_student_report(name, total, percentage, grade, passed)
    display_report(report)


if __name__ == "__main__":
    # Test run
    sample_name = "Alice Smith"
    sample_marks = [85.0, 92.0, 78.0, 88.0]
    total_possible = 400.0

    process_student(sample_name, sample_marks, total_possible)