import json
import os
from student import Student

DATA_FILE = os.path.join("data", "students.json")


def save_students(students):
    try:
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump([s.to_dict() for s in students], f, indent=4)
    except OSError as error:
        print("Could not save data:", error)
    else:
        print("Data saved.")


def load_students():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Data file is damaged. Starting empty.")
        return []
    else:
        return [Student.from_dict(item) for item in data]