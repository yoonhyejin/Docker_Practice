import requests
import json
from pendulum import timezone

url = 'http://0.0.0.0:5000/insert'

def insert_data(text):
    requests.post(url=url, data={ 'text' : text })
    
insert_data(text='First data using test_func')
