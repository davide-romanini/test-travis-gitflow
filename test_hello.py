from hello import hello

def test_hello():
    assert hello("David") == "Hello David, welcome"
    assert hello("Foo") == "Hello Foo, welcome"