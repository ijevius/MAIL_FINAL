# syntax=docker/dockerfile:1

FROM python:3.9.5-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY .. .
#CMD [ "python3.9", "app.py"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8083"]