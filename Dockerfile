FROM python:3.8.9-buster

WORKDIR /fhir-mapper

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /fhir-mapper .

CMD ["python", "fhir-mapper.py"]


