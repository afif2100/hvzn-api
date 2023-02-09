#app.py
from fastapi import FastAPI, Body, Request


# definisi dari app
app = FastAPI()


#membuat endpoint home, dengan method get
@app.get("/")
def home():
    return {"msg":"hello world"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

class PredictSalary():
    
    def __init__(self) -> None:
        self.base_salary = 5000000
        self.age_salary_multiplier = 50000
        
    def calculate_salary(self, age):
        return self.base_salary + (age * self.age_salary_multiplier)