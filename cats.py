import requests

"""
    token — telegram bot token
    clients — telegram user ids
"""

token = ''
clients = ['', ]

url = 'http://aws.random.cat/meow'
response = requests.get(url)
json = response.json()
cat = json['file']

for client in clients:
    request = requests.post(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={client}&photo={cat}')
