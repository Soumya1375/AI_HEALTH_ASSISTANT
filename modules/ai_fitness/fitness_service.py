"""
=========================================
AI Fitness Planner Service
=========================================

Author: Soumyadip
Project: AI Health Assistant

Features:
- AI Workout Planner
- Weight Loss Plans
- Muscle Gain Plans
- Fitness Maintenance Plans
- Beginner to Advanced

Powered By:
Gemini AI

=========================================
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

from modules.chatbot.gemini_client import ask_gemini


# =========================================
# FITNESS GOALS
# ==========================================

FITNESS_GOALS = [
    "Weight Loss",
    "Muscle Gain",
    "Stay Fit"
]

FITNESS_LEVELS = [
    "Beginner",
    "Intermediate",
    "Advanced"
]


# =========================================
# PROMPT BUILDER
# ==========================================

def build_fitness_prompt(
    age,
    gender,
    weight,
    height,
    goal,
    fitness_level
):
    """
    Build fitness planner prompt
    """

    prompt = f"""
You are a certified fitness trainer.

Create a professional 7-day fitness plan.

User Information:

Age: {age}
Gender: {gender}
Weight: {weight} kg
Height: {height} cm

Goal: {goal}
Fitness Level: {fitness_level}

Requirements:

1. Create a 7-day workout schedule.
2. Include warm-up exercises.
3. Include cardio if needed.
4. Include strength training if needed.
5. Include rest and recovery days.
6. Beginner-friendly explanations.
7. Mention approximate workout duration.

Format:

Day 1:
Workout:
Duration:

Day 2:
Workout:
Duration:

...

Finally provide:

- Safety Tips
- Motivation Tips
- Fitness Advice

Keep the response clear and professional.
"""

    return prompt


# =========================================
# GENERATE FITNESS PLAN
# ==========================================

def generate_fitness_plan(
    age,
    gender,
    weight,
    height,
    goal,
    fitness_level
):
    """
    Generate AI fitness plan
    """

    try:

        prompt = build_fitness_prompt(
            age=age,
            gender=gender,
            weight=weight,
            height=height,
            goal=goal,
            fitness_level=fitness_level
        )

        response = ask_gemini(prompt)

        return response

    except Exception as error:

        return f"""
❌ Error Generating Fitness Plan

Details:
{error}

Please try again.
"""


# =========================================
# QUICK FITNESS SCORE
# ==========================================

def calculate_fitness_score(
    bmi
):
    """
    Simple fitness score based on BMI
    """

    try:

        bmi = float(bmi)

        if 18.5 <= bmi <= 24.9:
            return 95

        elif 25 <= bmi <= 29.9:
            return 75

        elif bmi >= 30:
            return 55

        else:
            return 65

    except:
        return 0


# =========================================
# FITNESS STATUS
# ==========================================

def get_fitness_status(
    bmi
):

    try:

        bmi = float(bmi)

        if bmi < 18.5:
            return "Underweight"

        elif bmi < 25:
            return "Healthy"

        elif bmi < 30:
            return "Overweight"

        else:
            return "Obese"

    except:
        return "Unknown"


# =========================================
# TEST MODE
# ==========================================

if __name__ == "__main__":

    result = generate_fitness_plan(
        age=22,
        gender="Male",
        weight=72,
        height=175,
        goal="Weight Loss",
        fitness_level="Beginner"
    )

    print(result)

    print("\n------------------------\n")

    print(
        "Fitness Score:",
        calculate_fitness_score(24.5)
    )

    print(
        "Status:",
        get_fitness_status(24.5)
    )