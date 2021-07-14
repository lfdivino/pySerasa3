from pytest import fixture

from .constantes import STRING_REQUEST_CREDNET, RESULT_STRING_CREDNET
from pyserasa3.crednet import Crednet


@fixture()
def crednet():
    return Crednet("12345678", "45678901")


def test_create_crednet_with_login_and_password(crednet):
    assert crednet._login and crednet._password


def test_login_different_from_8_numbers():
    crednet = Crednet("123", "12345678")
    assert "Login and password must have 8 numbers!" in crednet.errors


def test_password_different_from_8_numbers():
    crednet = Crednet("12345678", "123")
    assert "Login and password must have 8 numbers!" in crednet.errors


def test_get_request_string(crednet):
    document_num = "12345678901"
    assert crednet._get_request_string(document_num) == STRING_REQUEST_CREDNET


def test_request_to_serasa(crednet, mocker):
    mocker.patch(
        'pyserasa3.crednet.requests.post',
        return_value=RESULT_STRING_CREDNET
    )
    document_num = "12345678901"
    crednet.request_serasa(document_num)
    assert crednet._original == RESULT_STRING_CREDNET.text
