from project import ext, neat, clean

def test_ext():
    assert ext("bye") is True
    assert ext("exit") is True
    assert ext("good night") is True
    assert ext("hello") is False
    assert ext("biscuit") is False

def test_neat():
    assert neat("  david  ") == "David"
    assert neat("biscuit") == "Biscuit"
    assert neat("ABHI") == "Abhi"

def test_clean():
    assert clean("  I Want To Play!  ") == "i want to play!"
    assert clean("BARK") == "bark"
