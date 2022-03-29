import main
import pytest



@pytest.mark.parametrize("num,output",[(5,True),(2,False),(10,True),(7,False)])
def test_divby5_1(num,output):
    result = main.divby5(num)
    assert result == output


@pytest.mark.parametrize("num,output",[(14,True),(20,False),(49,True),(2,False)])
def test_divby7_1(num,output):
         result = main.divby7(num)
         assert result == output

@pytest.mark.parametrize("num,output",[(45,True),(12,False),(90,True),(7,False)])
def test_divby9_1(num,output):
    result = main.divby9(num)
    assert result == output

@pytest.mark.parametrize("num,output",[(121,True),(12,False),(110,True),(7,False)])
def test_divby11_1(num,output):
    result = main.divby11(num)
    assert result == output

