from dataclasses import dataclass, field
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str


@dataclass
class Student:
    name: str
    age: int
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class Group:
    specialty: Specialty
    students: list[Student] = field(default_factory=list)


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0

    for group in groups:
        students_count = len(group.students)

        if students_count > max_students:
            max_students = students_count

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

    return list(
        {
            group.specialty.name
            for group in groups
        }
    )


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

    return students
