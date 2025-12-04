from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Numeric,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import relationship

# Змінюємо шлях на recruitment
from my_project.recruitment.utils.db import Base


class EnglishLevel(Base):
    __tablename__ = "english_levels"

    level_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)

    # Зв'язок один-до-багатьох (One EnglishLevel -> Many Candidates)
    candidates = relationship("Candidate", back_populates="english_level")

    def to_dict(self) -> dict:
        return {
            "level_id": self.level_id,
            "name": self.name,
        }


class TechLevel(Base):
    __tablename__ = "tech_levels"

    tech_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)

    candidates = relationship("Candidate", back_populates="tech_level")

    def to_dict(self) -> dict:
        return {
            "tech_id": self.tech_id,
            "name": self.name,
        }


class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    location = Column(String(100))

    # Зв'язок з проектами (One Company -> Many Projects)
    projects = relationship("Project", back_populates="company")

    def to_dict(self, include_projects: bool = False) -> dict:
        data = {
            "company_id": self.company_id,
            "name": self.name,
            "location": self.location,
        }
        if include_projects:
            data["projects"] = [p.to_dict() for p in self.projects]
        return data


class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)

    company = relationship("Company", back_populates="projects")
    # Зв'язок з вакансіями (One Project -> Many Vacancies)
    vacancies = relationship("Vacancy", back_populates="project")

    def to_dict(self, include_vacancies: bool = False) -> dict:
        data = {
            "project_id": self.project_id,
            "company_id": self.company_id,
            "name": self.name,
            "description": self.description,
        }
        if include_vacancies:
            data["vacancies"] = [v.to_dict() for v in self.vacancies]
        return data


class Vacancy(Base):
    __tablename__ = "vacancies"

    vacancy_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    salary_from = Column(Numeric(10, 2))
    salary_to = Column(Numeric(10, 2))

    project = relationship("Project", back_populates="vacancies")
    # Зв'язок з заявками (One Vacancy -> Many Applications)
    applications = relationship("Application", back_populates="vacancy")

    def to_dict(self) -> dict:
        return {
            "vacancy_id": self.vacancy_id,
            "project_id": self.project_id,
            "title": self.title,
            "description": self.description,
            "salary_from": float(self.salary_from) if self.salary_from else None,
            "salary_to": float(self.salary_to) if self.salary_to else None,
        }


class Candidate(Base):
    __tablename__ = "candidates"

    candidate_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100))
    email = Column(String(100), unique=True)
    phone = Column(String(20), unique=True)
    english_level_id = Column(Integer, ForeignKey("english_levels.level_id"))
    tech_level_id = Column(Integer, ForeignKey("tech_levels.tech_id"))
    experience_years = Column(Integer)

    english_level = relationship("EnglishLevel", back_populates="candidates")
    tech_level = relationship("TechLevel", back_populates="candidates")
    
    # Зв'язок з заявками (One Candidate -> Many Applications)
    applications = relationship("Application", back_populates="candidate")

    def to_dict(self) -> dict:
        data = {
            "candidate_id": self.candidate_id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "english_level_id": self.english_level_id,
            "tech_level_id": self.tech_level_id,
            "experience_years": self.experience_years,
        }
        # Додатково можна підтягнути назви рівнів, якщо вони завантажені
        if self.english_level:
            data["english_level"] = self.english_level.name
        if self.tech_level:
            data["tech_level"] = self.tech_level.name
            
        return data


class Application(Base):
    """
    Таблиця зв'язку М:М (Candidates <-> Vacancies)
    """
    __tablename__ = "applications"

    application_id = Column(Integer, primary_key=True, autoincrement=True)
    candidate_id = Column(Integer, ForeignKey("candidates.candidate_id"), nullable=False)
    vacancy_id = Column(Integer, ForeignKey("vacancies.vacancy_id"), nullable=False)
    applied_date = Column(Date)

    candidate = relationship("Candidate", back_populates="applications")
    vacancy = relationship("Vacancy", back_populates="applications")

    def to_dict(self) -> dict:
        return {
            "application_id": self.application_id,
            "candidate_id": self.candidate_id,
            "vacancy_id": self.vacancy_id,
            "applied_date": self.applied_date.isoformat() if self.applied_date else None,
        }

    # Спеціальні методи для зручного відображення (як у machine_product_controller)
    def to_vacancy_info_dict(self) -> dict:
        """Повернути інформацію про вакансію для цього кандидата"""
        return {
            "application_id": self.application_id,
            "applied_date": self.applied_date.isoformat() if self.applied_date else None,
            "vacancy": self.vacancy.to_dict() if self.vacancy else None
        }

    def to_candidate_info_dict(self) -> dict:
        """Повернути інформацію про кандидата для цієї вакансії"""
        return {
            "application_id": self.application_id,
            "applied_date": self.applied_date.isoformat() if self.applied_date else None,
            "candidate": self.candidate.to_dict() if self.candidate else None
        }