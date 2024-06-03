from schema import factory
from schema import Employee


j1 = Employee(employee_id = 1, first_name = "Harrier", last_name = "Debois", email ="tequillasunshine221@gmail.com", phone_number = "383838", hire_date = "17.04.1975", job_id = "1")
j2 = Employee(employee_id = 2, first_name = "Kim", last_name = "Katsuragi", email = "centristandy@gmail.com",phone_number = "898367363", hire_date= "10.15.1987", job_id = "1")


session = factory()
session.add_all([j1, j2])
session.commit()