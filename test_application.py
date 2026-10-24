from application import application


def test_lista_heroes():
    """Verifica que el endpoint retorne la lista de héroes."""

    response = application.test_client().get("/")

    assert response.status_code == 200
    assert "0" in response.get_json()


def test_un_heroe():
    """Verifica que se pueda consultar un héroe por su ID."""

    response = application.test_client().get("/0")

    assert response.status_code == 200
    assert response.get_json()["name"] == "A-Bomb"


def test_heroe_inexistente():
    """Verifica que un héroe inexistente retorne un error 404."""

    response = application.test_client().get("/9999")

    assert response.status_code == 404

