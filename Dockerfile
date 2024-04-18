FROM python:3.10-slim
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./templates /code/templates
COPY ./main.py /code
WORKDIR /code
CMD ["uvicorn","main:app","--host","0.0.0.0","--reload", "--port", "80"]
