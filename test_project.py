from devopslib.calc import add, sub, mul, div, power
from calCLI import cli

def test_add():
    assert add(1,2) == 3

#write a test for each function

def test_sub():
    assert sub(1,2) == -1

def test_mul():
    assert mul(1,2) == 2

def test_div():
    assert div(1,2) == 0.5


def test_power():
    assert power(2,3) == 8

