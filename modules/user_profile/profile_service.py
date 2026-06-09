"""
=========================================
User Profile Service
=========================================

Author: Soumyadip
Project: AI Health Assistant

Handles:
- Save User
- Get User
- Update User
- Delete User
- Get All Users

=========================================
"""

from database.db import (
    execute_query,
    fetch_one,
    fetch_all,
    insert_and_get_id
)


# =========================================
# CREATE USER
# =========================================

def create_user(
    name,
    age,
    gender,
    height,
    weight,
    blood_group
):
    """
    Create new user profile
    """

    query = """
    INSERT INTO users
    (
        name,
        age,
        gender,
        height,
        weight,
        blood_group
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """

    user_id = insert_and_get_id(
        query,
        (
            name,
            age,
            gender,
            height,
            weight,
            blood_group
        )
    )

    return user_id


# =========================================
# GET USER BY ID
# =========================================

def get_user_by_id(user_id):
    """
    Fetch single user
    """

    query = """
    SELECT *
    FROM users
    WHERE id = ?
    """

    return fetch_one(
        query,
        (user_id,)
    )


# =========================================
# GET ALL USERS
# =========================================

def get_all_users():
    """
    Fetch all users
    """

    query = """
    SELECT *
    FROM users
    ORDER BY created_at DESC
    """

    return fetch_all(query)


# =========================================
# UPDATE USER
# =========================================

def update_user(
    user_id,
    name,
    age,
    gender,
    height,
    weight,
    blood_group
):
    """
    Update user profile
    """

    query = """
    UPDATE users
    SET
        name = ?,
        age = ?,
        gender = ?,
        height = ?,
        weight = ?,
        blood_group = ?
    WHERE id = ?
    """

    return execute_query(
        query,
        (
            name,
            age,
            gender,
            height,
            weight,
            blood_group,
            user_id
        )
    )


# =========================================
# DELETE USER
# =========================================

def delete_user(user_id):
    """
    Delete user
    """

    query = """
    DELETE FROM users
    WHERE id = ?
    """

    return execute_query(
        query,
        (user_id,)
    )


# =========================================
# GET LATEST USER
# =========================================

def get_latest_user():
    """
    Return latest created user
    """

    query = """
    SELECT *
    FROM users
    ORDER BY id DESC
    LIMIT 1
    """

    return fetch_one(query)


# =========================================
# CHECK USER EXISTS
# =========================================

def user_exists(user_id):
    """
    Check if user exists
    """

    query = """
    SELECT id
    FROM users
    WHERE id = ?
    """

    user = fetch_one(
        query,
        (user_id,)
    )

    return user is not None


# =========================================
# TEST MODE
# =========================================

if __name__ == "__main__":

    user_id = create_user(
        name="Test User",
        age=22,
        gender="Male",
        height=1.75,
        weight=70,
        blood_group="O+"
    )

    print(f"\nUser Created: {user_id}")

    user = get_user_by_id(user_id)

    print("\nUser Details:")
    print(dict(user))

    users = get_all_users()

    print(f"\nTotal Users: {len(users)}")