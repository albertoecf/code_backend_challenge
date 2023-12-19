from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path


app = FastAPI()
test_file_path = Path( "tests/test_report/test_report.csv") 

@app.get("/")
def hello_handler():
    return {"msg": "Hello, World!"}

#todo define a proper view
@app.get("/report")
def read_report():   
    return FileResponse(test_file_path)