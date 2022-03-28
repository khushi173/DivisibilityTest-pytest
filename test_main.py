import main


def test_divby5_1():
    a = 25
    result = main.divby5(a)
    assert result == True

def test_divby5_2():
        a = 19
        result = main.divby5(a)
        assert result == False

def test_divby7_1():
         a = 14
         result = main.divby7(a)
         assert result == True

def test_divby5_2():
        a = 3
        result = main.divby7(a)
        assert result == False
def test_divby9_1():
    a = 54
    result = main.divby9(a)
    assert result == True

def test_divby9_2():
        a = 19
        result = main.divby9(a)
        assert result == False
def test_divby11_1():
    a = 121
    result = main.divby11(a)
    assert result == True

def test_divby11_2():
        a = 12
        result = main.divby11(a)
        assert result == False