APP_NAME = "AI Health Assistant"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = (
    "An AI-powered Health Assistant for symptom checking, "
    "BMI calculation, health guidance, and report analysis."
)

DATABASE_NAME = "health.db"

GENDER_OPTIONS = ["Male", "Female", "Other"]
BLOOD_GROUPS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

BMI_UNDERWEIGHT = 18.5
BMI_NORMAL = 24.9
BMI_OVERWEIGHT = 29.9

BMI_CATEGORIES = {
    "Underweight": (0, 18.4),
    "Normal": (18.5, 24.9),
    "Overweight": (25.0, 29.9),
    "Obese": (30.0, 100)
}

COMMON_SYMPTOMS = [
    "Fever", "Cough", "Headache", "Fatigue", "Vomiting",
    "Nausea", "Chest Pain", "Sore Throat", "Shortness of Breath", "Dizziness"
]

EMERGENCY_KEYWORDS = [
    "heart attack", "stroke", "chest pain", "unconscious",
    "breathing difficulty", "difficulty breathing", "severe bleeding",
    "seizure", "allergic reaction"
]

EMERGENCY_MESSAGE = """
🚨 MEDICAL EMERGENCY DETECTED

The symptoms described may indicate a serious medical condition.

Please seek immediate medical attention or contact local emergency services.

This AI assistant cannot replace professional medical care.
"""

IMPORTANT_MEDICAL_PARAMETERS = [
    "Hemoglobin", "Glucose", "Blood Sugar", "Cholesterol",
    "WBC", "RBC", "Platelet", "Creatinine", "Urea", "Vitamin D"
]

MAX_CHAT_HISTORY = 50

SYSTEM_PROMPT = """
You are an AI Health Assistant.

Your responsibilities:
1. Provide educational health information.
2. Explain diseases and symptoms simply.
3. Explain medical reports.
4. Suggest healthy lifestyle habits.

Important Rules:
- Do not provide final medical diagnoses.
- Do not prescribe medicines.
- Always recommend consulting a doctor for serious concerns.
- Keep answers clear and concise.
"""

ALLOWED_FILE_TYPES = ["pdf"]
MAX_FILE_SIZE_MB = 10

SIDEBAR_MENU = [
    "🏠 Home",
    "👤 User Profile",
    "⚖️ BMI Calculator",
    "🤖 AI Chatbot",
    "🩺 Symptom Checker",
    "📊 Health Dashboard",
    "📄 Report Analyzer"
]

DEFAULT_CHART_HEIGHT = 400

PROFILE_SAVED = "✅ Profile saved successfully."
BMI_SAVED = "✅ BMI record saved successfully."
REPORT_UPLOADED = "✅ Report uploaded successfully."
CHAT_SAVED = "✅ Chat history saved successfully."

ERROR_EMPTY_NAME = "❌ Name cannot be empty."
ERROR_INVALID_AGE = "❌ Age must be greater than 0."
ERROR_INVALID_HEIGHT = "❌ Height must be greater than 0."
ERROR_INVALID_WEIGHT = "❌ Weight must be greater than 0."
ERROR_PDF_ONLY = "❌ Please upload a PDF file only."