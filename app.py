import requests
import json
from datetime import datetime, timezone
import random
import config

base_url = 'https://petstore.swagger.io/v2'

# GET /user/login  Logs user into the system

username = config.username
password = config.password

res = requests.get(f'{base_url}/user/login?login={username}&password={password}',
                   headers={'accept': 'application/json'})

print('GET /user/login  Logs user into the system')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json())
print('  Ответ сервера header:', res.headers, '\n')


# POST /pet  Add a new pet to the store

body = config.new_pet
body['name'] = 'Mango'  # Имя питомца
body['category']['name'] = 'python'
body['tags'][0]['name'] = 'carnivorous'  # Метка добавляемого питомца
body['tags'].append({"id": 0, "name": "long snake"})
body['status'] = 'test_status'  # Статус для тестирования, используется дальше
body = json.dumps(body)

res = requests.post(f'{base_url}/pet', headers={'accept': 'application/json',
                                                'Content-Type': 'application/json'}, data=body)

petid = res.json()['id']

print('POST /pet  Add a new pet to the store')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# GET /pet/findByStatus  Finds Pets by status

status = 'test_status'

res = requests.get(f'{base_url}/pet/findByStatus?status={status}', headers={'accept': 'application/json'})

print('GET /pet/findByStatus  Finds Pets by status')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# PUT /pet  Update an existing pet

body = config.new_pet
body['id'] = petid  # Указываем id питомца которого надо обновить
body['name'] = 'Mangos'  # Новое имя питомца
body['category']['name'] = 'python'
body['tags'][0]['name'] = 'carnivorous'
body['tags'].append({"id": 1, "name": "very long snake"})
body['status'] = 'test_status'  # Статус не трогаем
body = json.dumps(body)

res = requests.put(f'{base_url}/pet', headers={'accept': 'application/json',
                                               'Content-Type': 'application/json'}, data=body)

print('PUT /pet  Update an existing pet')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# POST /pet/{petId}/uploadImage  Uploads an image

petId = petid
image = 'python.jpg'
files = {'file': (image, open(image, 'rb'), 'image/jpeg')}

res = requests.post(f'{base_url}/pet/{petId}/uploadImage', headers={'accept': 'application/json'}, files=files)

print('POST /pet/{petId}/uploadImage  Uploads an image')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')


# GET /pet/{petId}  Find pet by ID

petId = petid

res = requests.get(f'{base_url}/pet/{petId}', headers={'accept': 'application/json'})

print('GET /pet/{petId}  Find pet by ID')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')


# POST /pet/{petId}  Updates a pet in the store with form data

petId = petid
name = 'Mangos2'
status = 'new_test_status'
body = f'name={name}&status={status}'

res = requests.post(f'{base_url}/pet/{petId}', headers={'accept': 'application/json',
                                                        'Content-Type': 'application/x-www-form-urlencoded'}, data=body)

print('POST /pet/{petId}  Updates a pet in the store with form data')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')


# DELETE /pet/{petId}  Deletes a pet

petId = petid

res = requests.delete(f'{base_url}/pet/{petId}', headers={'accept': 'application/json'})

print('DELETE /pet/{petId}  Deletes a pet')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')
