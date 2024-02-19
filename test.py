import pytest
from main import StudentsInMLOps

def test_enroll_students():
    ops = StudentsInMLOps()
    ops.enrollStudents(5)
    assert ops.getTotalStrength() == 5

def test_drop_students():
    ops = StudentsInMLOps()
    ops.enrollStudents(10)
    ops.dropStudents(3)
    assert ops.getTotalStrength() == 7

def test_get_class_name():
    ops = StudentsInMLOps()
    assert ops.getClassName() == "StudentsInMLOps"
