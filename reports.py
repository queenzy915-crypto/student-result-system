from results import calculate_total, calculate_average, assign_grade


def student_summary(student):
    total = calculate_total(student.scores)
    average = calculate_average(student.scores)
    grade = assign_grade(average)
    return total, average, grade


def list_students(students):
    if not students:
        print("No students registered.")
        return
    print(f"{'ID':<10}{'Name':<22}{'Total':>8}{'Average':>10}{'Grade':>7}")
    for s in students:
        total, average, grade = student_summary(s)
        print(f"{s.student_id:<10}{s.name:<22}{total:>8}{average:>10.2f}{grade:>7}")


def sort_by_average(students):
    return sorted(students, key=lambda s: calculate_average(s.scores), reverse=True)


def sort_by_name(students):
    return sorted(students, key=lambda s: s.name.lower())


def report_card(student):
    total, average, grade = student_summary(student)
    print("\n===== REPORT CARD =====")
    print("ID:", student.student_id)
    print("Name:", student.name)
    print("Class:", student.form)
    print("Gender:", student.gender)
    print("Date of birth:", student.dob)
    print("-----------------------")
    for subject, score in student.scores.items():
        print(f"{subject:<20}{score}")
    print("-----------------------")
    print("Total:", total)
    print(f"Average: {average:.2f}")
    print("Grade:", grade)
    print("Result entered:", student.date_entered)


def class_statistics(students):
    scored = [s for s in students if s.scores]
    if not scored:
        print("No scores recorded yet.")
        return
    averages = [calculate_average(s.scores) for s in scored]
    totals = [calculate_total(s.scores) for s in scored]
    print("\n===== CLASS STATISTICS =====")
    print("Highest total:", max(totals))
    print("Lowest total:", min(totals))
    print(f"Class average: {sum(averages) / len(averages):.2f}")


def save_report(students, filename="report.txt"):
    try:
        with open(filename, "w") as f:
            f.write("STUDENT RESULT REPORT\n")
            f.write("=====================\n")
            for s in sort_by_average(students):
                total, average, grade = student_summary(s)
                f.write(f"{s.student_id} | {s.name} | Total: {total} | "
                        f"Average: {average:.2f} | Grade: {grade}\n")
    except OSError as error:
        print("Could not save report:", error)
    else:
        print("Report saved to", filename)