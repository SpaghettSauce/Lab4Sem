from schema import factory
from schema import Job


j1 = Job(job_title="Spoon licker", min_salary=15000, max_salary=35000)
j2 = Job(job_title="Penquin seerer", min_salary=80000, max_salary=95000)
j3 = Job(job_title="Juice drinker", min_salary=20000, max_salary=25000)
j4 = Job(job_title="Dumb Programmer", min_salary=10000, max_salary=11000)

session = factory()
session.add_all([j1, j2, j3, j4])
session.commit()