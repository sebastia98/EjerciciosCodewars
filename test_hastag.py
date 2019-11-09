from hastag import generate_hashtag


def test_uno():
    assert generate_hashtag("") == False


def test_dos():
    assert generate_hashtag("hola") == "#Hola"


def test_tres():
    assert generate_hashtag("Hola") == "#Hola"


def test_cuatro():
    assert generate_hashtag("hola que tal") == "#HolaQueTal"
