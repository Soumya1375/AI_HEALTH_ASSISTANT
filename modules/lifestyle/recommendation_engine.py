"""
=========================================
Lifestyle Recommendation Engine
=========================================

Author: Soumyadip
Project: AI Health Assistant

Features:
- BMI Based Recommendations
- Diet Suggestions
- Exercise Plans
- Health Tips

=========================================
"""


# =========================================
# GET RECOMMENDATION
# =========================================

def get_recommendation(bmi):
    """
    Return personalized lifestyle
    recommendation based on BMI
    """

    try:

        bmi = float(bmi)

    except:

        return {
            "category": "Unknown",
            "diet": [],
            "exercise": [],
            "tips": []
        }

    # =====================================
    # UNDERWEIGHT
    # =====================================

    if bmi < 18.5:

        return {

            "category": "Underweight",

            "diet": [
                "🥚 Eggs",
                "🥛 Milk",
                "🧀 Paneer",
                "🍗 Chicken",
                "🥜 Nuts & Dry Fruits",
                "🍌 Banana"
            ],

            "exercise": [
                "🏋️ Light Strength Training",
                "🚶 20 Minutes Walking",
                "🤸 Stretching Exercises"
            ],

            "tips": [
                "Increase healthy calorie intake",
                "Eat 5-6 small meals daily",
                "Sleep 7-9 hours regularly",
                "Stay hydrated"
            ]
        }

    # =====================================
    # NORMAL
    # =====================================

    elif bmi < 25:

        return {

            "category": "Normal Weight",

            "diet": [
                "🥗 Balanced Diet",
                "🍎 Fruits",
                "🥦 Vegetables",
                "🍚 Whole Grains",
                "🥛 Dairy Products"
            ],

            "exercise": [
                "🚶 30 Minutes Walking",
                "🏃 Light Jogging",
                "🚴 Cycling"
            ],

            "tips": [
                "Maintain current routine",
                "Drink enough water",
                "Avoid excessive junk food",
                "Continue regular exercise"
            ]
        }

    # =====================================
    # OVERWEIGHT
    # =====================================

    elif bmi < 30:

        return {

            "category": "Overweight",

            "diet": [
                "🥗 Low Calorie Foods",
                "🥦 More Vegetables",
                "🍎 Fruits",
                "🍗 Lean Protein",
                "🚫 Reduce Sugary Drinks"
            ],

            "exercise": [
                "🚶 45 Minutes Walking",
                "🏃 Cardio Exercise",
                "🚴 Cycling"
            ],

            "tips": [
                "Maintain calorie deficit",
                "Avoid processed foods",
                "Track daily calorie intake",
                "Exercise regularly"
            ]
        }

    # =====================================
    # OBESE
    # =====================================

    else:

        return {

            "category": "Obese",

            "diet": [
                "🥦 High Fiber Foods",
                "🥗 Controlled Portions",
                "🍎 Fruits",
                "🍗 Lean Protein",
                "🚫 Avoid Fast Food"
            ],

            "exercise": [
                "🚶 60 Minutes Walking",
                "🏊 Swimming",
                "🚴 Low Impact Cardio"
            ],

            "tips": [
                "Consult healthcare professional",
                "Focus on gradual weight loss",
                "Maintain healthy diet plan",
                "Monitor BMI regularly"
            ]
        }


# =========================================
# FORMAT RECOMMENDATION
# =========================================

def format_recommendation(bmi):
    """
    Return formatted recommendation text
    """

    recommendation = get_recommendation(bmi)

    output = f"\n📊 Category: {recommendation['category']}\n"

    output += "\n🍽 Recommended Diet:\n"

    for item in recommendation["diet"]:
        output += f"• {item}\n"

    output += "\n🏃 Recommended Exercise:\n"

    for item in recommendation["exercise"]:
        output += f"• {item}\n"

    output += "\n💡 Health Tips:\n"

    for item in recommendation["tips"]:
        output += f"• {item}\n"

    return output


# =========================================
# TEST MODE
# =========================================

if __name__ == "__main__":

    bmi = 27.5

    result = format_recommendation(bmi)

    print(result)