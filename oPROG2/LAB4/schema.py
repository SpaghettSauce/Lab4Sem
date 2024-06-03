from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Numeric

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Basis(DeclarativeBase):
    pass


class Country(Basis):
    __tablename__ = "countries"
    country_id = Column(Integer(), primary_key=True, autoincrement=True)
    country_name = Column(String(), unique=True, nullable=False)
    region_id = Column(Integer(), ForeignKey('regions.region_id'))

    regions = relationship("Region", back_populates="country_place",
                           cascade="all, delete")

    def __str__(self):
        return f"<{self.country_id}> {self.country_name} {self.region_id}"

    def __repr__(self):
        return f"{self.country_id} ({self.country_name} {self.region_id})"


class Department(Basis):
    __tablename__ = "departments"
    department_id = Column(Integer(), primary_key=True, autoincrement=True)
    department_name = Column(String(), nullable=False)
    manager_id = Column(Integer(), ForeignKey('employees.employee_id'))
    location_id = Column(Integer(), ForeignKey('locations.location_id'))

    workers = relationship("Employee", back_populates="employee_dep",
                           cascade="all, delete")

    location = relationship("Location", back_populates="department",
                           cascade="all, delete")

    def __str__(self):
        return f"<{self.department_id}> {self.department_name} {self.manager_id} {self.location_id}"

    def __repr__(self):
        return f"<{self.department_id}> {self.department_name} {self.manager_id} {self.location_id}"


class Employee(Basis):
    __tablename__ = "employees"
    employee_id = Column(Integer(), primary_key=True, autoincrement=True)
    first_name = Column(String())
    last_name = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    phone_number = Column(String())
    hire_date = Column(String(), nullable=False)
    job_id = Column(String(), ForeignKey('jobs.job_id'), nullable=False)
    salary = Column(Numeric())
    commission_pct = Column(Numeric())
    manager_id = Column(Integer(), ForeignKey('employees.employee_id'))
    department_id = Column(Integer())

    jobs = relationship("Job", back_populates="employee",
                           cascade="all, delete")

    employee_dep = relationship("Department", back_populates="workers",
                           cascade="all, delete")

    def __str__(self):
        return f"<{self.employee_id}> {self.first_name} {self.last_name} {self.email} {self.phone_number} " \
               f"{self.hire_date} {self.job_id} {self.salary} {self.commission_pct} {self.manager_id} {self.department_id}"

    def __repr__(self):
        return f"{self.employee_id} {self.first_name} {self.last_name} {self.email} {self.phone_number} " \
               f"{self.hire_date} {self.job_id} {self.salary} {self.commission_pct} {self.manager_id} {self.department_id}"


class JobGrades(Basis):
    __tablename__ = "job_grades"
    grade_level = Column(String(), primary_key=True)
    lowest_sal = Column(Integer())
    highest_sal = Column(Integer())

    def __str__(self):
        return f"<{self.grade_level}> {self.lowest_sal}: {self.highest_sal}"

    def __repr__(self):
        return f"<{self.grade_level}> {self.lowest_sal}: {self.highest_sal}"

class JobHistory(Basis):
    __tablename__ = "job_history"
    employee_id = Column(Integer(), primary_key=True)
    start_date = Column(String(), nullable=False)
    end_date = Column(String(), nullable=False)
    job_id = Column(String(), ForeignKey('jobs.job_id'), nullable=False)
    department_id = Column(Integer())

    job = relationship("Job", back_populates="job_history",
                           cascade="all, delete")

    def __str__(self):
        return f"<{self.employee_id}> {self.start_date} {self.end_date} {self.job_id} {self.department_id}"

    def __repr__(self):
        return f"<{self.employee_id}> {self.start_date} {self.end_date} {self.job_id} {self.department_id}"


class Job(Basis):
    __tablename__ = "jobs"
    job_id = Column(Integer(), primary_key=True, autoincrement=True)
    job_title = Column(String(), nullable=False)
    min_salary = Column(Integer())
    max_salary = Column(Integer())

    employee = relationship("Employee", back_populates="jobs",
                        cascade="all, delete")
    job_history = relationship("JobHistory", back_populates="job",
                       cascade="all, delete")

    def __str__(self):
        return f"<{self.job_id}> {self.job_title}: {self.min_salary} {self.max_salary}"

    def __repr__(self):
        return f"<{self.job_id}> {self.job_title}: {self.min_salary} {self.max_salary}"

class Location(Basis):
    __tablename__ = "locations"
    location_id = Column(Integer(), primary_key=True, autoincrement=True)
    street_address = Column(String())
    postal_code = Column(String())
    city = Column(String(), nullable=False)
    state_province = Column(String())
    country_id = Column(String())

    department = relationship("Department", back_populates="location",
                            cascade="all, delete")

    def __str__(self):
        return f"<{self.location_id}> {self.street_address} {self.postal_code} {self.city} {self.state_province} {self.country_id}"

    def __repr__(self):
        return f"<{self.location_id}> {self.street_address} {self.postal_code} {self.city} {self.state_province} {self.country_id}"


class Region(Basis):
    __tablename__ = "regions"
    region_id = Column(Integer(), primary_key=True, autoincrement=True)
    region_name = Column(String(), unique=True, nullable=False)

    country_place = relationship("Country", back_populates="regions",
                           cascade="all, delete")

    def __str__(self):
        return f"<{self.region_id}> {self.region_name}"

    def __repr__(self):
        return f"<{self.region_id}> {self.region_name}"


engine = create_engine("sqlite:///Database/Staff.db?echo=True")

Basis.metadata.create_all(engine)

factory = sessionmaker(bind=engine)
