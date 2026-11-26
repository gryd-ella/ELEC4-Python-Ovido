# Name: Mariella Ovido
# Section: IV-BSIT C
# Activity: P2 - Custom Module
# Date: November 18, 2026

def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASS"
    else:
        return "FAIL"
