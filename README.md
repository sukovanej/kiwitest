Installation

```
cd currency_converter_directory
sudo pip install .
```

Running server

```
sudo docker build -t currency_converter .
sudo docker run -d -p 5000:5000 --name currency_converter currency_converter
```

Unittests

```
python -m unittest discover tests/
```
