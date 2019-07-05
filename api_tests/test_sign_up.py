import pytest
import time
import requests
import json

from constants import BASE_URL, SUCCESSFULLY_CREATED, UNPROCESSABLE_ENTITY, USER_ALREADY_EXIST_ERROR


def test_sign_up_positive_scenario():
    # generate unique email using current timestamp
    email = f"email{int(time.time())}@example.com"
    body = {
        "email": email,
        "password": "qwerty1",
        "confirm_password": "qwerty1"
    }
    headers = {
        "content-type": "application/json"
    }
    r = requests.post(url=f'{BASE_URL}/auth/register', data=json.dumps(body), headers=headers)
    # check status code
    assert SUCCESSFULLY_CREATED == r.status_code
    # check email from response
    assert email == r.json()["user"]["email"]


def test_sign_up_negative_scenario():
    body = {
        "email": "email@example.com",
        "password": "qwerty1",
        "confirm_password": "qwerty1"
    }
    headers = {
        "content-type": "application/json"
    }
    r = requests.post(url=f'{BASE_URL}/auth/register', data=json.dumps(body), headers=headers)
    assert UNPROCESSABLE_ENTITY == r.status_code
    # check expected error
    assert USER_ALREADY_EXIST_ERROR == r.json()['errors']


#  Задача
#  Расширить функциональность тестов параметризоваными фикстурами. Написать 2 варианта тестовых данных для первого теста
#  и 4 варианта для второго. Фикстуры должны отдавать в тест данные и ожидаемый результат. Потом изменить код тестов,
#  Так чтобы они заработали
#