FROM ubuntu:18.04

WORKDIR /FarmerMarket

# Update apt packages
RUN apt update
RUN apt upgrade -y

# Install vim
RUN apt install vim -y

# Install python 3.7
RUN apt install python3.7 -y

# Make python 3.7 the default
RUN echo "alias python=python3.7" >> ~/.bashrc
RUN export PATH=${PATH}:/usr/bin/python3.7
RUN /bin/bash -c "source ~/.bashrc"

# Install pip
RUN apt install python3-pip -y
RUN python3 -m pip install --upgrade pip


COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY src/ .
COPY Tests/ .

CMD [ "python3", "./PlaceOrder.py" ]

CMD ["sleep", "infinity"]
