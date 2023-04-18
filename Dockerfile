FROM python:3.11.3-alpine3.17

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
