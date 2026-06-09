"""
=========================================
Symptom Checker Engine
=========================================

Author: Soumyadip
Project: AI Health Assistant

This module:
- Loads symptoms.json
- Loads diseases.json
- Matches symptoms
- Predicts possible conditions
- Returns disease details

=========================================
"""

import json
from collections import Counter

from config.settings import SYMPTOMS_JSON, DISEASES_JSON


# =========================================
# LOAD JSON FILES
# =========================================

def load_symptoms_data():
    """
    Load symptom mapping data
    """
    try:
        with open(SYMPTOMS_JSON, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception as e:
        print(f"Error loading symptoms.json: {e}")
        return {}


def load_diseases_data():
    """
    Load disease information
    """
    try:
        with open(DISEASES_JSON, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception as e:
        print(f"Error loading diseases.json: {e}")
        return {}


# =========================================
# GET POSSIBLE CONDITIONS
# =========================================

def analyze_symptoms(selected_symptoms):
    """
    Analyze user selected symptoms

    Parameters:
        selected_symptoms (list)

    Returns:
        list of possible conditions
    """

    symptoms_data = load_symptoms_data()

    disease_counter = Counter()

    for symptom in selected_symptoms:

        if symptom in symptoms_data:

            diseases = symptoms_data[symptom]

            for disease in diseases:
                disease_counter[disease] += 1

    if not disease_counter:
        return []

    sorted_conditions = disease_counter.most_common()

    return sorted_conditions


# =========================================
# GET DISEASE DETAILS
# =========================================

def get_disease_details(disease_name):
    """
    Return disease information
    """

    diseases_data = load_diseases_data()

    return diseases_data.get(disease_name, {})


# =========================================
# FULL ANALYSIS
# =========================================

def generate_analysis(selected_symptoms):
    """
    Full symptom analysis

    Returns:
        [
            {
                disease,
                match_score,
                description,
                advice
            }
        ]
    """

    conditions = analyze_symptoms(selected_symptoms)

    results = []

    for disease, score in conditions:

        disease_info = get_disease_details(disease)

        results.append(
            {
                "disease": disease,
                "match_score": score,
                "description": disease_info.get(
                    "description",
                    "No description available."
                ),
                "advice": disease_info.get(
                    "advice",
                    "Consult a healthcare professional."
                )
            }
        )

    return results


# =========================================
# EMERGENCY CHECK
# =========================================

def check_emergency(selected_symptoms):
    """
    Detect emergency symptoms
    """

    emergency_symptoms = [
        "Chest Pain",
        "Shortness of Breath",
        "Unconscious"
    ]

    for symptom in selected_symptoms:

        if symptom in emergency_symptoms:
            return True

    return False


# =========================================
# TEST MODE
# =========================================

if __name__ == "__main__":

    test_symptoms = [
        "Fever",
        "Cough",
        "Fatigue"
    ]

    result = generate_analysis(test_symptoms)

    print("\nPossible Conditions:\n")

    for item in result:

        print(
            f"{item['disease']} "
            f"(Match Score: {item['match_score']})"
        )

        print(item["description"])
        print(item["advice"])
        print("-" * 50)