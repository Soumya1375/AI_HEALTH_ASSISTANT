"""
=========================================
Medicine Reminder Service
=========================================

Author: Soumyadip
Project: AI Health Assistant

Features:
- Add Reminder
- Get All Reminders
- Delete Reminder

=========================================
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

from database.db import (
    execute_query,
    fetch_all
)


# =========================================
# ADD REMINDER
# =========================================

def add_reminder(
    medicine_name,
    reminder_time
):
    """
    Add new medicine reminder
    """

    query = """
    INSERT INTO medicine_reminders
    (
        medicine_name,
        reminder_time
    )
    VALUES (?, ?)
    """

    return execute_query(
        query,
        (
            medicine_name,
            reminder_time
        )
    )


# =========================================
# GET ALL REMINDERS
# =========================================

def get_all_reminders():
    """
    Fetch all reminders
    """

    query = """
    SELECT *
    FROM medicine_reminders
    ORDER BY id DESC
    """

    return fetch_all(query)


# =========================================
# DELETE REMINDER
# =========================================

def delete_reminder(
    reminder_id
):
    """
    Delete reminder by ID
    """

    query = """
    DELETE FROM medicine_reminders
    WHERE id = ?
    """

    return execute_query(
        query,
        (reminder_id,)
    )


# =========================================
# GET REMINDER COUNT
# =========================================

def get_reminder_count():

    reminders = get_all_reminders()

    return len(reminders)


# =========================================
# TEST MODE
# =========================================

if __name__ == "__main__":

    print("\n💊 Medicine Reminder Test\n")

    add_reminder(
        "Paracetamol",
        "09:00 AM"
    )

    reminders = get_all_reminders()

    for reminder in reminders:

        try:

            print(
                reminder["medicine_name"],
                "-",
                reminder["reminder_time"]
            )

        except:

            print(reminder)

    print(
        f"\nTotal Reminders: {get_reminder_count()}"
    )