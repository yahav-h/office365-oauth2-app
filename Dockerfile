FROM python:3.8

WORKDIR /app

COPY ./resources /app/resources
COPY ./resources/properties.yml /app/resources/properties.yml
COPY ./helpers.py /app/helpers.py
COPY ./dto.py /app/dto.py
COPY ./dao.py /app/dao.py
COPY ./locators.py /app/locators.py
COPY ./database.py /app/database.py
COPY ./dependencies.txt /app/dependencies.txt
COPY ./o365_Auth.py /app/o365_Auth.py
COPY ./o365_Service.py /app/o365_Service.py
COPY ./logs/runtime.log /app/logs/runtime.log

RUN pip install -r /app/dependencies.txt

EXPOSE 80

CMD python o365_Service.py
