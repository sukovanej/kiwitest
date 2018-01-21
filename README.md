Running

```
docker-compose up
```

This commands starts 3 services - redis, currency_converter and forex
downloader. Currency_converter is public and can be used by typing
(for example)

```
curl '127.0.0.1:5000/currrency_converter?amonut=200&input_currency=USD'
```
