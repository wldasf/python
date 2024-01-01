import pytest
from employee import Employee

@pytest.fixture
def employee_salary():
    return Employee('waleed', 'assaf', 5000)

def test_give_default_raise(employee_salary):
    employee_salary.give_raise()
    assert employee_salary.annual_salary == 10000

def test_give_custom_raise(employee_salary):
    employee_salary.give_raise(7000)
    assert employee_salary.annual_salary == 12000
