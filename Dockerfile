FROM alpine:latest
MAINTAINER yagermadden@gmail.com

RUN apk update && apk add \
    python \
    python-dev \
    py-pip

RUN mkdir /oblique
WORKDIR /oblique

COPY oblique.py /oblique/oblique.py
RUN chmod +x /oblique/oblique.py
COPY *.txt /oblique/

RUN pip install -r requirements.txt

RUN rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

EXPOSE 80 

CMD ["gunicorn", "-b", "0.0.0.0:80", "oblique:app", "--log-file=-"]
