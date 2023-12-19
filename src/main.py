from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_handler():
    return {"msg": "Hello, World!"}
