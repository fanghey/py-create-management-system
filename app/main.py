from datetime import datetime
import dataclasses
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: "Specialty"
    course: int
    students: list["Student"] = field(default_factory=list)



def write_groups_information(groups):
    max_students = 0

    for group in groups:
        students_count = len(getattr(group, "students", []))
        if students_count > max_students:
            max_students = students_count

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max_students


def write_students_information(students):
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information():
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

    return list({
        getattr(group, "specialty", None)
        for group in groups
        if hasattr(group, "specialty")
    } - {None})


def read_students_information():
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

    return students# write your code here
