from employee import Employee

def test_give_default_raise():
    emp = Employee('waleed', 'assaf', 5000)
    emp.give_raise()
    assert emp.annual_salary == 10000

def test_give_custom_raise():
    emp = Employee('waleed', 'assaf', 7000)
    emp.give_raise(7000)
    assert emp.annual_salary == 14000
