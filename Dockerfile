FROM python:3.10

WORKDIR /FarmerMarket

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY FarmerMarket/ .

CMD [ "python3", "./PlaceOrder.py" ]
