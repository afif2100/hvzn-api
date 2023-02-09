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

