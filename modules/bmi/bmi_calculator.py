"""
=========================================
BMI Calculator Engine
=========================================

Author: Soumyadip
Project: AI Health Assistant

Handles:
- BMI Calculation
- BMI Category Detection
- BMI Advice Generation

=========================================
"""

import json

from config.settings import BMI_RANGES_JSON


# =========================================
# LOAD BMI DATA
# =========================================

def load_bmi_ranges():
    """
    Load BMI ranges from JSON file
    """

    try:

        with open(
            BMI_RANGES_JSON,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception as error:

        print(
            f"Error loading BMI data: {error}"
        )

        return {}


# =========================================
# CALCULATE BMI
# =========================================

def calculate_bmi(
    height,
    weight
):
    """
    BMI Formula

    BMI = Weight / Height²

    Parameters:
        height (meters)
        weight (kg)

    Returns:
        float
    """

    try:

        bmi = weight / (height ** 2)

        return round(bmi, 2)

    except ZeroDivisionError:

        return 0.0


# =========================================
# GET BMI CATEGORY
# =========================================

def get_bmi_category(bmi):
    """
    Determine BMI category
    """

    bmi_ranges = load_bmi_ranges()

    for category, details in bmi_ranges.items():

        if (
            details["min"]
            <= bmi
            <= details["max"]
        ):

            return {
                "category": category,
                "status": details["status"],
                "message": details["message"]
            }

    return {
        "category": "Unknown",
        "status": "Unknown",
        "message": "BMI category unavailable."
    }


# =========================================
# FULL BMI ANALYSIS
# =========================================

def analyze_bmi(
    height,
    weight
):
    """
    Complete BMI Analysis
    """

    bmi = calculate_bmi(
        height,
        weight
    )

    category_data = get_bmi_category(
        bmi
    )

    return {
        "bmi": bmi,
        "category": category_data["category"],
        "status": category_data["status"],
        "message": category_data["message"]
    }


# =========================================
# TEST MODE
# =========================================

if __name__ == "__main__":

    result = analyze_bmi(
        height=1.75,
        weight=70
    )

    print("\nBMI Analysis\n")

    print(
        f"BMI: {result['bmi']}"
    )

    print(
        f"Category: {result['category']}"
    )

    print(
        f"Status: {result['status']}"
    )

    print(
        f"Message: {result['message']}"
    )