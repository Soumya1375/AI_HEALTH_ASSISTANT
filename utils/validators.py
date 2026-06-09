def validate_username(username):
    return username is not None and len(username) >= 3


def validate_password(password):
    return password is not None and len(password) >= 4


def validate_bmi_input(weight, height):
    return weight > 0 and height > 0