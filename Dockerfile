FROM ubuntu:14.04
MAINTAINER yagermadden@gmail.com

RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    python-pip

RUN mkdir /oblique
WORKDIR /oblique

COPY oblique.py /oblique/oblique.py
RUN chmod +x /oblique/oblique.py
COPY *.txt /oblique/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "oblique:app", "--log-file=-"]
# CMD ["python", "oblique.py"]