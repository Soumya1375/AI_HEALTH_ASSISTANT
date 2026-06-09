"""
=========================================
Database Connection Manager
=========================================

Author: Soumyadip
Project: AI Health Assistant

Handles:
- SQLite Connection
- Query Execution
- Fetch Operations
- Database Initialization

=========================================
"""

import sqlite3

from config.settings import DATABASE_PATH


# =========================================
# DATABASE CONNECTION
# =========================================

def get_connection():
    """
    Create and return SQLite connection
    """

    try:

        connection = sqlite3.connect(
            DATABASE_PATH,
            check_same_thread=False
        )

        connection.row_factory = sqlite3.Row

        return connection

    except sqlite3.Error as error:

        print(
            f"Database Connection Error: {error}"
        )

        return None


# =========================================
# EXECUTE QUERY
# =========================================

def execute_query(query, params=None):
    """
    INSERT / UPDATE / DELETE

    Returns:
        True / False
    """

    connection = get_connection()

    if connection is None:
        return False

    try:

        cursor = connection.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        connection.commit()

        return True

    except sqlite3.Error as error:

        print(
            f"Database Query Error: {error}"
        )

        return False

    finally:

        connection.close()


# =========================================
# FETCH ONE
# =========================================

def fetch_one(query, params=None):
    """
    Fetch single row
    """

    connection = get_connection()

    if connection is None:
        return None

    try:

        cursor = connection.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        result = cursor.fetchone()

        return result

    except sqlite3.Error as error:

        print(
            f"Database Fetch Error: {error}"
        )

        return None

    finally:

        connection.close()


# =========================================
# FETCH ALL
# =========================================

def fetch_all(query, params=None):
    """
    Fetch multiple rows
    """

    connection = get_connection()

    if connection is None:
        return []

    try:

        cursor = connection.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        results = cursor.fetchall()

        return results

    except sqlite3.Error as error:

        print(
            f"Database Fetch Error: {error}"
        )

        return []

    finally:

        connection.close()


# =========================================
# INSERT AND RETURN ID
# =========================================

def insert_and_get_id(query, params=None):
    """
    Insert record and return row id
    """

    connection = get_connection()

    if connection is None:
        return None

    try:

        cursor = connection.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        connection.commit()

        return cursor.lastrowid

    except sqlite3.Error as error:

        print(
            f"Database Insert Error: {error}"
        )

        return None

    finally:

        connection.close()


# =========================================
# DATABASE HEALTH CHECK
# =========================================

def test_database_connection():
    """
    Check database connectivity
    """

    try:

        connection = get_connection()

        if connection:

            connection.close()

            return True

        return False

    except Exception:

        return False


# =========================================
# TEST MODE
# =========================================

if __name__ == "__main__":

    if test_database_connection():

        print(
            "✅ Database Connected Successfully"
        )

    else:

        print(
            "❌ Database Connection Failed"
        )