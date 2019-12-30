FROM alpine

COPY requirements.txt .
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py2-pip \
 && pip2 install --upgrade pip \
 && pip2 install flask

COPY server.py .
COPY CariBeach.jpg .
EXPOSE 8000
CMD ["python", "./server.py"]

