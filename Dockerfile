FROM python:3.9

COPY ./ApiPeliculas /app

RUN pip3 install -r app/requirements.txt

WORKDIR /app/src

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]