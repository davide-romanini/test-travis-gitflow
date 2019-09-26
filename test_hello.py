from hello import hello, add, minus

def test_hello():
    assert hello("David") == "Hello David, welcome"
    assert hello("John") == "Hello John, welcome"
    assert hello("Matt") == "Hello Matt, welcome"
    assert hello("Joe") == "Hello Joe, welcome"

def test_add():
    assert add(5, 1) == 6

def test_minus():
    assert minus(5, 1) == 4