import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '97adca82badb988fbb0ad1545b836873'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN }
trainer_id = 18430

def test_status_code(): 
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : trainer_id}) 
    assert response.status_code == 200

def test_my_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : trainer_id})
    assert response.json().get('data')[0].get('trainer_name') == 'Auto'