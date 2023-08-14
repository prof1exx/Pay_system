FROM python:latest

WORKDIR /pay_system

COPY . /pay_systems

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]
