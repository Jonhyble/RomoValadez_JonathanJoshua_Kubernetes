from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import database as connection
import requests

from database import Administrador, Pelicula, Usuario, Generos, Usuario_Pelicula, Administrador_Pelicula, Genero_Pelicula

app = FastAPI()

@app.on_event("startup")
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([  Administrador,
                                Pelicula,
                                Usuario,
                                Generos,
                                Usuario_Pelicula,
                                Administrador_Pelicula,
                                Genero_Pelicula])
    print("Bonjour")


@app.on_event("shutdown")
def shutdown():
    if not connection.is_closed():
        connection.close()
    print("Arrive Derchi")


@app.get("/")
async def root():
    response = requests.get('https://api.publicapis.org/entries')

    print(response.json())
    return {"message": "Hello World"}