from hello import hello

def test_hello():
    assert hello("David") == "Hello David, welcome"
    assert hello("John") == "Hello John, welcome"
    assert hello("Matt") == "Hello Matt, elcome"