from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def teste_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/olamundo')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Hello World</h1>' in response.text
