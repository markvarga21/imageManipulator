FROM ubuntu

COPY . ./app
COPY requirements.txt /app/
COPY ./resources/ /app/

WORKDIR /app

RUN apt-get update && apt-get install -y tesseract-ocr
RUN apt install wget -y
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0.0_1.0.2n-1ubuntu5_amd64.deb
RUN dpkg -i libssl1.0.0_1.0.2n-1ubuntu5_amd64.deb
RUN apt install python3-pip -y
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt install libssl-dev -y
RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]