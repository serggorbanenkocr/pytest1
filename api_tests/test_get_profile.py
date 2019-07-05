import pytest
import requests
import json
from constants import *


@pytest.fixture(scope='function')
def logged_user():
    pass


def test_get_my_profile(logged_user):
    r = requests.get(url=f'{BASE_URL}/users/me', headers={"Authorization": logged_user["session"]["access_token"]})
    assert SUCCESS == r.status_code
    assert logged_user["user"]["id"] == r.json()["id"]


# Задача
# Написать код фикстуры logged_user. Должна авторизовать юзера, вернуть респонс в тест, выполнить логаут после теста
# Фикстуру написать в двух вариантах с использованием addfinalizer и через yield