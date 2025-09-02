from fastapi import FastAPI
from fastapi.responses import JSONResponse

from pieql import pieql


app = FastAPI()


@app.get("/items")
@pieql()
def items():
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Carol"}
        ]
    }
