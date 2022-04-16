FROM python:3.8

WORKDIR /FarmerMarket

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY FarmerMarket/ .
