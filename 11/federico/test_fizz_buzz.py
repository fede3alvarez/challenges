import pytest
import fizz_buzz as fb

# Test Fizz
#@pytest.mark.parametrize(["a", "b"], [(1, 1), (3, "Fizz")])
#def test_fizz_buzz_1(a, b):
#    assert b == fb.fizz_buzz(a)

def test_fizz_buzz_2():
    assert "Buzz" == fb.fizz_buzz(5)

def test_fizz_buzz_3():
    assert "Fizz Buzz" == fb.fizz_buzz(30)

#def test_fizz_buzz_4():
#    assert -1 == fb.fizz_buzz("Ketchup")

def f_AssertionError():
    raise AssertionError(1)

def test_fizz_buzz_5():
    with pytest.raises(AssertionError):
        f_AssertionError()