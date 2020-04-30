import pytest
import requests

url = 'http://127.0.0.1:5000' # The root url of the flask app

def test_get_by_app_id():
    response = requests.get(url + '/GetMessage?application_id=1') 
    assert response.status_code == 200
def test_get_by_session_id():
    response = requests.get(url + '/GetMessage?session_id=aaa') 
    assert response.status_code == 200
def test_get_by_message_id():
    response = requests.get(url + '/GetMessage?message_id=bbb')
    assert response.status_code == 200
def test_by_no_args():
    response = requests.get(url + '/GetMessage')
    assert response.status_code == 200
def test_by_multiple_args():
    response = requests.get(url + '/GetMessage?application_id=1&session_id=kkk')
    assert response.status_code == 200