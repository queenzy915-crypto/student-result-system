import re
from datetime import datetime


def is_valid_id(student_id):
    """Check the ID is 3-10 letters or numbers (uses regex)."""
    return re.match(r"^[A-Za-z0-9]{3,10}$", student_id) is not None


class Student:
    def __init__(self, student_id, name, form, gender, dob,
                 scores=None, date_entered=None):
        self.student_id = student_id
        self.name = name
        self.form = form
        self.gender = gender
        self.dob = dob
        self.scores = scores if scores else {}
        self.date_entered = date_entered

    def set_score(self, subject, score):
        """Add or update one subject score and record the date."""
        self.scores[subject] = score
        self.date_entered = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        """Turn the student into a dictionary so it can be saved as JSON."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "form": self.form,
            "gender": self.gender,
            "dob": self.dob,
            "scores": self.scores,
            "date_entered": self.date_entered,
        }

    @staticmethod
    def from_dict(data):
        """Rebuild a Student from a saved dictionary."""
        return Student(
            data["student_id"], data["name"], data["form"],
            data["gender"], data["dob"],
            data.get("scores", {}), data.get("date_entered"),
        )