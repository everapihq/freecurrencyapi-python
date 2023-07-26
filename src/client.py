import everapi


class Client(everapi.Client):
    def __init__(self, api_key, base='https://api.freecurrencyapi.com/v1'):
        super(Client, self).__init__(base, api_key)

    def status(self):
        return self._request('/status')

    def currencies(self, currencies=[]):
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        return self._request('/currencies', params={
            'currencies': self._list_to_comma_seperated(currencies)
        })

    def latest(self, base_currency=None, currencies=[]):
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        return self._request('/latest', params={
            'base_currency': base_currency,
            'currencies': self._list_to_comma_seperated(currencies)
        })

    def historical(self, date, base_currency=None, currencies=[]):
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        return self._request('/historical', params={
            'date': date,
            'base_currency': base_currency,
            'currencies': self._list_to_comma_seperated(currencies)
        })

    def _list_to_comma_seperated(self, lst):
        return ','.join(lst)
