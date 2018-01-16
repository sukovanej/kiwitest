FROM python:3
WORKDIR /usr/src/currency_converter

COPY requirements.txt ./
RUN pip install .

COPY . .
CMD [ "./scripts/currency_converter_server" ]
