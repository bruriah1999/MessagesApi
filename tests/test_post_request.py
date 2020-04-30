import pytest
import requests

url = 'http://127.0.0.1:5000' #flask app url 

def test_post_msg1():
    data = {
        "application_id": 3, 
        "session_id": "ddd",
        "message_id": "hhh",
        "participants": ["Shlomo", "Shalom"],
        "content": "Where are you now?"
    }
    response = requests.post(url + '/AddMessage', json=data)
    assert response.status_code == 200
def test_post_msg2():
    data = {
        "application_id": 1, 
        "session_id": "aaa",
        "message_id": "bbb",
        "participants": ["Moshe Cohen", "Avi Aviv"],
        "content": "Hello, how are you today?"
    }
    response = requests.post(url + '/AddMessage', json=data)
    assert response.status_code == 200

def test_missing_prop_in_json():
    data = {
        "session_id": "ccc",
        "message_id": "ddd",
        "participants": ["Uri Levi", "Meir Rokah"],
        "content": "Hello, how are you today?"
    }
    response = requests.post(url + '/AddMessage', json=data)
    assert response.status_code == 200

def test_non_uniqe_id():
    response = None
    data = {
        "application_id": 7, 
        "session_id": "fff",
        "message_id": "ggg",
        "participants": ["David Ben Gurion", "Menahem Begin"],
        "content": "Have a great day"
    }
    response = requests.post(url + '/AddMessage', json=data)
    if response.status_code == 200:
        data = {
            "application_id": 7, 
            "session_id": "fff",
            "message_id": "ggg",
            "participants": ["David Ben Gurion", "Menahem Begin"],
            "content": "Have a great day"
        }
        response = requests.post(url + '/AddMessage', json=data)
    assert response.status_code == 200
