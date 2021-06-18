from pytest import fixture

from .constantes import STRING_CONSULTA_CREDNET
from pyserasa3.crednet import Crednet


@fixture()
def crednet():
    return Crednet("12345678", "45678901")


def test_create_crednet_with_login_and_password(crednet):
    assert crednet._login and crednet._password


def test_login_must_be_8_numbers(crednet):
    assert len(crednet._login) == 8


def test_password_must_be_8_numbers(crednet):
    assert len(crednet._password) == 8


def test_login_different_from_8_numbers():
    crednet = Crednet("123", "12345678")
    assert "Login e password devem possuir 8 números!" in crednet.errors


def test_password_different_from_8_numbers():
    crednet = Crednet("12345678", "123")
    assert "Login e password devem possuir 8 números!" in crednet.errors


def test_get_request_string(crednet):
    num_documento = "12345678901"
    assert crednet._get_request_string(num_documento) == STRING_CONSULTA_CREDNET
