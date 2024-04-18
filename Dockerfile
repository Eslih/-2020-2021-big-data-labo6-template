FROM python:3.12.3-alpine3.19

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
