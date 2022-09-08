from typing import Union
from urllib import response

from fastapi import FastAPI  
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    a: int
    b: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/Addition")
def add(input_vars: Item):
    result = (input_vars.a + input_vars.b)
    return {"Result": result}

@app.post("/Subtraction")
def sub(input_vars: Item):
    result = (input_vars.a - input_vars.b)
    return {"Result": result}

@app.post("/Multiplication")
def mul(input_vars: Item):
    result = (input_vars.a * input_vars.b)
    return {"Result": result}

@app.post("/Division")
def div(input_vars:Item):
    try:
        return {"Result" : input_vars.a / input_vars.b}
    except ZeroDivisionError:
        return {"Sorry!! You are dividing by zero"}
