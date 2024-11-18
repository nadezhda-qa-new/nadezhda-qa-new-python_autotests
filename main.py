import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '97adca82badb988fbb0ad1545b836873'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN }

'''body_registration = {
    "trainer_token": TOKEN,
    "email": "kolo_so@mail.ru",
    "password": "Ilona_2016"
}

body_confirmation = {
    "trainer_token": TOKEN,
}
'''
body_create = {
    "name": "Бульбаз",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "139224",
    "name": "Бульбик",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "139224"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''# создание покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
'''

'''# изменение имени
response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)'''

# поймать в покебол

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)