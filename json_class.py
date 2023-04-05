import json
import requests
from pprint import pprint
import climage

data = '''
[
    {'id':'001',
    'x':'2',
    'name':'Chuck'},

    {'id':'019',
    'x':'10',
    'name':'Benice',
    'skills':['A','B','C']}
]'''

info = json.loads(data)
for p in info:
    print(p)
    print(p['skills'][0]) if 'skills' in p else ...


BASE_ENDPOINT = 'https://fakestoreapi.com/'
url = 'products/'
CART_ENDPOINT = 'carts/'

post_data = {
    'title': 'Benice',
    'price': 1.5,
    'description': 'lorem ipsum set',
    'image': 'https://i.pravatar.cc',
    'categories': 'electronic'
}


response = requests.post(url, json=post_data)
data = response.json()
pprint(data, indent=4)

print(climage.convert("https://i.pravatar.cc"))
