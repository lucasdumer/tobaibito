FROM debian:10

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python-gtk2
RUN apt-get install -y python-gtk2-dev
RUN apt-get install -y afnix
RUN apt-get install python3-gi
RUN apt-get install -y python3-gi gir1.2-wnck-3.0
RUN apt-get install -y python3-pip
RUN apt-get install libjpeg-dev zlib1g-dev
RUN pip3 install Pillow
RUN pip3 install python3-xlib
RUN pip3 install pynput

WORKDIR /src

COPY ./src .

RUN ls

CMD ["python3", "./main.py"]