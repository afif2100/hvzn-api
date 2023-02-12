# app.py
from fastapi import FastAPI, Body, Request
from pydantic import BaseModel


# definisi dari app
app = FastAPI()


# membuat endpoint home, dengan method get
@app.get("/")
def home():
    return {"msg": "hello world"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# membuat data model
class Person(BaseModel):
    name: str = "Fulan"


@app.post("/hello")
def hello(person: Person):
    return f"Hello, {person.name}"


# # Membuat Prediction model
# class PredictSalary:
#     def __init__(self) -> None:
#         self.base_salary = 5000000
#         self.age_salary_multiplier = 50000

#     def calculate_salary(self, age):
#         return self.base_salary + (age * self.age_salary_multiplier)


# ps = PredictSalary()

# # membuat data model
# class Person(BaseModel):
#     # nama variabel:tipe data
#     name: str
#     age: int


# @app.post("/predict")
# def predict_salary(employee: Person):
#     salary = ps.calculate_salary(employee.age)
#     return {"name": employee.name, "salary": salary}
