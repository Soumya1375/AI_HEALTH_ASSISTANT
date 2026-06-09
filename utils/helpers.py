import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate_bmi(weight, height):
    if height == 0:
        return 0
    return round(weight / (height ** 2), 2)