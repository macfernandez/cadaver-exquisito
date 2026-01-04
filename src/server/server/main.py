from fastapi import FastAPI

from server.models import Model
from server.schemas import Text


app = FastAPI()


@app.get("/")
def welcome():
    return {"text": "Welcome to the Cadaver Exquisito API"}


@app.post("/chat", response_model=Text)
def generate(text: Text) -> Text:
    response = Model().generate(text.text)
    return Text(text=response)
