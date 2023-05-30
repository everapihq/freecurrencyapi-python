# freecurrencyapi Python Client #

Freecurrencyapi Python Client is the official Python Wrapper around the freecurrencyapi [API](https://freecurrencyapi.com/).

## Installation

Install from pip:
````sh
pip install freecurrencyapi
````

Install from code:
````sh
pip install git+https://github.com/everapihq/freecurrencyapi-python.git
````

## Usage

All freecurrencyapi API requests are made using the `Client` class. This class must be initialized with your API access key string. [Where is my API access key?](https://app.freecurrencyapi.com/dashboard)

In your Python application, import `freecurrencyapi` and pass authentication information to initialize it:

````python
import freecurrencyapi
client = freecurrencyapi.Client('API_KEY')
````

### Retrieve Status

```python

print(client.status())

```

### Retrieve Currencies
[https://freecurrencyapi.com/docs/currencies](https://freecurrencyapi.com/docs/currencies)
```python

result = client.currencies(currencies=['EUR', 'CAD'])
print(result)

```

### Retrieve Latest Exchange Rates
[https://freecurrencyapi.com/docs/latest](https://freecurrencyapi.com/docs/latest)

```python

result = client.latest()
print(result)

```

### Retrieve Historical Exchange Rates
[https://freecurrencyapi.com/docs/historical](https://freecurrencyapi.com/docs/historical)

```python

result = client.historical('2022-02-02')
print(result)

```

### Contact us
Any feedback? Please feel free to [contact our team](mailto:office@everapi.com).
