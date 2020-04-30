import pytest
import requests

url = 'http://127.0.0.1:5000' #flask app url 
def test_delete_by_app_id():
    response = requests.delete(url + '/DeleteMessage?application_id=1') 
    assert response.status_code == 200
def test_delete_by_session_id():
    response = requests.delete(url + '/DeleteMessage?session_id=aaa') 
    assert response.status_code == 200
def test_delete_by_message_id():
    response = requests.delete(url + '/DeleteMessage?message_id=bbb')
    assert response.status_code == 200
def test_by_no_args():
    response = requests.delete(url + '/DeleteMessage')
    assert response.status_code == 200
def test_by_multiple_args():
    response = requests.delete(url + '/DeleteMessage?application_id=1&session_id=kkk')
    assert response.status_code == 200