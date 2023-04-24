from fastapi import FastAPI
import requests

app = FastAPI()

@app.on_event("startup")
def startup():
    print("Bonjour")


@app.on_event("shutdown")
def shutdown():
    print("Arrive Derchi")


@app.get("/")
async def root():
    response = requests.get('https://api.publicapis.org/entries')

    print(response.json())
    return {"message": "Hello World"}