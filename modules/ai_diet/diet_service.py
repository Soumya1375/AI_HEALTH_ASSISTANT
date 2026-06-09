"""
=========================================
AI Diet Planner Service
=========================================

Author: Soumyadip
Project: AI Health Assistant

Features:
- Generate AI Diet Plan
- Weight Loss
- Weight Gain
- Maintain Weight

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
# PROMPT BUILDER
# =========================================

def build_diet_prompt(
    age,
    gender,
    weight,
    height,
    goal
):
    """
    Build AI Diet Prompt
    """

    prompt = f"""
You are a certified nutrition expert.

Create a healthy and practical diet plan.

User Details:

Age: {age}
Gender: {gender}
Weight: {weight} kg
Height: {height} cm

Goal: {goal}

Provide:

1. Breakfast
2. Mid-Morning Snack
3. Lunch
4. Evening Snack
5. Dinner

Rules:

- Simple foods
- Affordable foods
- Balanced nutrition
- Healthy lifestyle tips

Format nicely with headings.
"""

    return prompt


# =========================================
# GENERATE DIET PLAN
# =========================================

def generate_diet_plan(
    age,
    gender,
    weight,
    height,
    goal
):
    """
    Generate AI diet plan
    """

    try:

        prompt = build_diet_prompt(
            age,
            gender,
            weight,
            height,
            goal
        )

        response = ask_gemini(prompt)

        return response

    except Exception as error:

        return f"""
❌ Error Generating Diet Plan

{error}
"""


# =========================================
# TEST MODE
# =========================================

if __name__ == "__main__":

    result = generate_diet_plan(
        age=22,
        gender="Male",
        weight=75,
        height=172,
        goal="Weight Loss"
    )

    print(result)