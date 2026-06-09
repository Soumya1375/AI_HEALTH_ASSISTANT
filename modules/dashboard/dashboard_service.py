import sqlite3
from datetime import datetime, timedelta


# ==========================================
# DATABASE CONNECTION
# ==========================================
DB_PATH = "health_assistant.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


# ==========================================
# BASIC STATS (DASHBOARD KPIs)
# ==========================================
def get_total_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()[0]

    conn.close()
    return result


def get_total_bmi_records():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM bmi_records")
    result = cursor.fetchone()[0]

    conn.close()
    return result


def get_total_chat_sessions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM chat_history")
    result = cursor.fetchone()[0]

    conn.close()
    return result


# ==========================================
# BMI ANALYTICS
# ==========================================
def get_bmi_distribution():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, COUNT(*) 
        FROM bmi_records 
        GROUP BY category
    """)

    data = cursor.fetchall()
    conn.close()

    return data


# ==========================================
# RECENT ACTIVITY
# ==========================================
def get_recent_users(limit=5):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, age, gender 
        FROM users 
        ORDER BY id DESC 
        LIMIT ?
    """, (limit,))

    data = cursor.fetchall()
    conn.close()

    return data


def get_recent_chats(limit=5):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_message, bot_response 
        FROM chat_history 
        ORDER BY id DESC 
        LIMIT ?
    """, (limit,))

    data = cursor.fetchall()
    conn.close()

    return data


# ==========================================
# TIME-BASED ANALYTICS (optional future use)
# ==========================================
def get_records_last_days(table_name, days=7):
    conn = get_connection()
    cursor = conn.cursor()

    date_threshold = datetime.now() - timedelta(days=days)

    cursor.execute(f"""
        SELECT COUNT(*) 
        FROM {table_name}
        WHERE created_at >= ?
    """, (date_threshold,))

    result = cursor.fetchone()[0]
    conn.close()

    return result