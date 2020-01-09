FROM debian:buster-slim

WORKDIR /client/

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-venv \
  && apt-get install -y python3-pip

RUN python3 -m venv venv

# Install dependencies:
COPY requirements.txt /client/
RUN . venv/bin/activate && pip3 install -r requirements.txt

# Run the application:
ADD . /client/

CMD . venv/bin/activate && exec python3 client.py