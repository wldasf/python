import pytest
from employee import Employee

def test_give_default_raise():
    first_name = "waleed"
    last_name = "assaf"
    annual_salary = 5000
    give_raise = Employee(annual_salary)
    give_raise.give_raise(5000)
    assert 5000 in give_raise.annual_salary

def test_give_custom_raise():
    first_name = "waleed"
    last_name = "assaf"
    annual_salary = 7000
    give_raise = Employee(annual_salary)
    give_raise.give_raise(7000)
