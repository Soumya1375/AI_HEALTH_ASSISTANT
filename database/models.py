"""
=========================================
Database Models
=========================================

Author: Soumyadip
Project: AI Health Assistant

Creates:
1. users
2. bmi_records
3. chat_history
4. reports
5. medicine_reminders

=========================================
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from database.db import get_connection


# =========================================
# USERS TABLE
# =========================================

CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    age INTEGER NOT NULL,

    gender TEXT NOT NULL,

    height REAL NOT NULL,

    weight REAL NOT NULL,

    blood_group TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


# =========================================
# BMI RECORDS TABLE
# =========================================

CREATE_BMI_TABLE = """
CREATE TABLE IF NOT EXISTS bmi_records (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    height REAL NOT NULL,

    weight REAL NOT NULL,

    bmi REAL NOT NULL,

    category TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES users(id)
);
"""


# =========================================
# CHAT HISTORY TABLE
# =========================================

CREATE_CHAT_HISTORY_TABLE = """
CREATE TABLE IF NOT EXISTS chat_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    question TEXT NOT NULL,

    answer TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES users(id)
);
"""


# =========================================
# REPORTS TABLE
# =========================================

CREATE_REPORTS_TABLE = """
CREATE TABLE IF NOT EXISTS reports (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    file_name TEXT NOT NULL,

    extracted_text TEXT,

    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES users(id)
);
"""


# =========================================
# MEDICINE REMINDER TABLE
# =========================================

CREATE_MEDICINE_REMINDER_TABLE = """
CREATE TABLE IF NOT EXISTS medicine_reminders (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    medicine_name TEXT NOT NULL,

    reminder_time TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


# =========================================
# CREATE ALL TABLES
# =========================================

def create_tables():

    connection = None

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(CREATE_USERS_TABLE)

        cursor.execute(CREATE_BMI_TABLE)

        cursor.execute(CREATE_CHAT_HISTORY_TABLE)

        cursor.execute(CREATE_REPORTS_TABLE)

        cursor.execute(CREATE_MEDICINE_REMINDER_TABLE)

        connection.commit()

        print("✅ Database tables created successfully.")

    except Exception as error:

        print(
            f"❌ Error creating tables: {error}"
        )

    finally:

        if connection:
            connection.close()


# =========================================
# SHOW TABLES
# =========================================

def show_tables():

    connection = None

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table';
            """
        )

        tables = cursor.fetchall()

        print("\n📋 Available Tables:\n")

        for table in tables:

            try:
                print(table["name"])
            except:
                print(table[0])

    except Exception as error:

        print(
            f"❌ Error fetching tables: {error}"
        )

    finally:

        if connection:
            connection.close()


# =========================================
# MAIN
# =========================================

if __name__ == "__main__":

    create_tables()

    show_tables()