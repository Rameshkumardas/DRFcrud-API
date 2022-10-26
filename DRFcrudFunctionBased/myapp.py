import requests
import json


URL = "http://127.0.0.1:8000/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    request = requests.get(url=URL, headers= headers, data=json_data)
    data = request.json()
    print(data)
# get_data()

def post_data():
    data = {
        "full_name":"Aakriti",
        "email":"aakriti@gmail.com",
        "pNumber":"aakriti",
        "password":"aakriti",
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    request = requests.get(url=URL, headers= headers, data=json_data)
    data = request.json()
post_data()

def Put_Data():
    data = {
        "id":1,
        "full_name":"Aakriti",
        "email":"aakriti@gmail.com",
        "pNumber":98247587142,
        "password":"aakriti",
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    request = requests.get(url=URL, headers= headers, data=json_data)
    data = request.json()
    print(data)
# Put_Data()