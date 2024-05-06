
FROM python:3
MAINTAINER RomanTask 'https://github.com/RomanTask'
RUN apt-get update -qy
RUN apt-get install -qy python3.8 python3-pip python3.8-dev
COPY . .
WORKDIR . .
RUN apt-get install -y python3-pip
RUN apt-get update && apt-get install -y --no-install-recommends

RUN pip3 install flet easygui

CMD [ "python3", "main.py" , "runserver" ,"0.0.0.8000"]
