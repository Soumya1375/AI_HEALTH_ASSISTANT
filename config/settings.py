"""
=========================================
AI Health Assistant - Settings
=========================================
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# =========================================
# LOAD ENV FILE
# =========================================

load_dotenv()

# =========================================
# PROJECT ROOT
# =========================================

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================
# DATABASE SETTINGS
# =========================================

DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "health.db"

# Auto create database folder if missing
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

# =========================================
# UPLOAD SETTINGS
# =========================================

UPLOAD_DIR = BASE_DIR / "uploads"
REPORT_UPLOAD_DIR = UPLOAD_DIR / "reports"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
REPORT_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# =========================================
# ASSETS SETTINGS
# =========================================

ASSETS_DIR = BASE_DIR / "assets"

LOGO_PATH = ASSETS_DIR / "logo.png"
BANNER_PATH = ASSETS_DIR / "banner.png"
CSS_PATH = ASSETS_DIR / "styles.css"

# =========================================
# DATA FILES
# =========================================

DATA_DIR = BASE_DIR / "data"

BMI_RANGES_JSON = DATA_DIR / "bmi_ranges.json"
SYMPTOMS_JSON = DATA_DIR / "symptoms.json"
DISEASES_JSON = DATA_DIR / "diseases.json"

# =========================================
# GEMINI SETTINGS
# =========================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Recommended
GEMINI_MODEL = "gemini-2.5-flash"

# =========================================
# STREAMLIT SETTINGS
# =========================================

PAGE_TITLE = "AI Health Assistant"

PAGE_ICON = "🏥"

LAYOUT = "wide"

SIDEBAR_STATE = "expanded"

APP_CONFIG = {
    "page_title": PAGE_TITLE,
    "page_icon": PAGE_ICON,
    "layout": LAYOUT,
    "initial_sidebar_state": SIDEBAR_STATE
}

# =========================================
# CHAT SETTINGS
# =========================================

MAX_CHAT_HISTORY = 50

CHAT_TEMPERATURE = 0.4

MAX_RESPONSE_TOKENS = 1024

# =========================================
# FILE SETTINGS
# =========================================

ALLOWED_EXTENSIONS = ["pdf"]

MAX_UPLOAD_SIZE_MB = 10

# =========================================
# DEBUG
# =========================================

DEBUG = True

# =========================================
# SECURITY
# =========================================

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "ai-health-assistant-secret-key"
)