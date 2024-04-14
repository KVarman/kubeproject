FROM python:3.9

COPY poetry.lock pyproject.toml ./

RUN pip install poetry

RUN poetry install

COPY main.py ./

CMD ["poetry","run","uvicorn","main:app","--host", "0.0.0.0"]


EXPOSE 8000

