import requests
import json
from pendulum import timezone

url = 'http://localhost:5000/insert'

def insert_data(text):
    requests.post(url=url, data={ 'text' : text })
    
insert_data(text='First data using test_func')
