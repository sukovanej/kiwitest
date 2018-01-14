FROM python:3
WORKDIR /usr/src/currency_converter

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./currency_converter_run.py" ]
EXPOSE 5000
