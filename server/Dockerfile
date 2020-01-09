FROM debian:buster-slim

WORKDIR /server/

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-venv \
  && apt-get install -y python3-pip \
  && apt-get install -y libpq-dev

RUN python3 -m venv venv

# Install dependencies:
COPY requirements.txt /server/
RUN . venv/bin/activate && pip3 install -r requirements.txt

# Run the application:
ADD . /server/

CMD . venv/bin/activate && exec python3 server.py