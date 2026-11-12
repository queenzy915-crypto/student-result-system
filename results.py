def calculate_total(scores):
    return sum(scores.values())


def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return calculate_total(scores) / len(scores)


def assign_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    else:
        return "F"