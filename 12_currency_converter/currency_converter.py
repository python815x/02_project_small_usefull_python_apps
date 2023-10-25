import requests


access_key = '7ea85c592e96eb9386ff08676025e2c7'
base_currency = 'EUR'
symbols = 'USD'

# Make a request to the "latest" endpoint
url = f'http://api.exchangeratesapi.io/v1/latest?access_key={access_key}&{base_currency}&{symbols}'
response = requests.get(url)
exchange_rates = {}
if response.status_code == 200:
    data = response.json()
    exchange_rates = data['rates']
    print(exchange_rates)
else:
    print('Error fetching data.')


print(exchange_rates['AUD'])

