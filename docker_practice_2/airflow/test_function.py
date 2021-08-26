import requests
import json
from pendulum import timezone

url = 'http://localhost:5000/insert'

def insert_data(text):
    datas = { 'text' : text }
    x = requests.post(url=url, json=datas)
    print(x.text) 

insert_data(text='First data using test_func')
