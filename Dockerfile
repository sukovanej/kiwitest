FROM python:3
WORKDIR /usr/src/currency_converter

COPY . .
RUN pip install .

CMD [ "currency_converter_server" ]
