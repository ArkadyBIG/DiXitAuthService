FROM python:3.7-alpine3.17

WORKDIR /app

COPY dixit ./

RUN python3 -m pip install -r req.txt

EXPOSE 8083

CMD [ "python3", "main.py" ]
