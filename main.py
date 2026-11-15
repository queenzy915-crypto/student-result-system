from datetime import datetime
from student import Student, is_valid_id
from storage import save_students, load_students
from reports import (list_students, sort_by_average, sort_by_name,
                     report_card, class_statistics, save_report)


def find_student(students, student_id):
    for s in students:
        if s.student_id.lower() == student_id.lower():
            return s
    return None


def get_score(prompt="Score (0-100): "):
    try:
        score = float(input(prompt))
    except ValueError:
        print("Please enter a number.")
        return None
    else:
        if 0 <= score <= 100:
            return score
        print("Score must be between 0 and 100.")
        return None


def get_dob():
    dob = input("Date of birth (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return None
    return dob


def add_student(students):
    student_id = input("Student ID (3-10 letters/numbers): ").strip()
    if not is_valid_id(student_id):
        print("Invalid ID.")
        return
    if find_student(students, student_id):
        print("That ID already exists.")
        return
    name = input("Full name: ").strip()
    form = input("Class/Form: ").strip()
    gender = input("Gender: ").strip()
    dob = get_dob()
    if dob is None:
        return
    students.append(Student(student_id, name, form, gender, dob))
    save_students(students)
    print("Student added.")


def view_students(students):
    if not students:
        print("No students registered.")
        return
    for s in students:
        print(f"{s.student_id} | {s.name} | {s.form} | {s.gender} | {s.dob}")


def search_student(students):
    term = input("Enter ID or name: ").strip().lower()
    found = [s for s in students
             if term == s.student_id.lower() or term in s.name.lower()]
    if not found:
        print("No match found.")
        return
    for s in found:
        print(f"{s.student_id} | {s.name} | {s.form} | {s.gender} | {s.dob}")


def update_student(students):
    s = find_student(students, input("Student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    s.name = input(f"Name [{s.name}]: ").strip() or s.name
    s.form = input(f"Class [{s.form}]: ").strip() or s.form
    s.gender = input(f"Gender [{s.gender}]: ").strip() or s.gender
    s.dob = input(f"Date of birth [{s.dob}]: ").strip() or s.dob
    save_students(students)
    print("Student updated.")


def delete_student(students):
    s = find_student(students, input("Student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    students.remove(s)
    save_students(students)
    print("Student deleted.")


def record_scores(students):
    s = find_student(students, input("Student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    print("Enter at least 5 subjects. Type 'done' when finished.")
    while True:
        subject = input("Subject (or 'done'): ").strip()
        if subject.lower() == "done":
            if len(s.scores) < 5:
                print("You need at least 5 subjects.")
                continue
            break
        score = get_score()
        if score is not None:
            s.set_score(subject, score)
    save_students(students)


def update_score(students):
    s = find_student(students, input("Student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    subject = input("Subject to update: ").strip()
    if subject not in s.scores:
        print("That subject has no score yet.")
        return
    score = get_score("New score (0-100): ")
    if score is not None:
        s.set_score(subject, score)
        save_students(students)
        print("Score updated.")


def show_report_card(students):
    s = find_student(students, input("Student ID: ").strip())
    if s is None:
        print("Student not found.")
    else:
        report_card(s)


def list_sorted(students):
    choice = input("Sort by 1) average or 2) name: ").strip()
    if choice == "1":
        list_students(sort_by_average(students))
    else:
        list_students(sort_by_name(students))


def menu():
    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Record scores")
    print("7. Update a score")
    print("8. Student report card")
    print("9. List students with results")
    print("10. Class statistics")
    print("11. Save text report")
    print("0. Exit")


def main():
    students = load_students()
    while True:
        menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            record_scores(students)
        elif choice == "7":
            update_score(students)
        elif choice == "8":
            show_report_card(students)
        elif choice == "9":
            list_sorted(students)
        elif choice == "10":
            class_statistics(students)
        elif choice == "11":
            save_report(students)
        elif choice == "0":
            save_students(students)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()