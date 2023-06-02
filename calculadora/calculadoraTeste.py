import calculadora
import pytest


def test_add():
    assert calculadora.add(2, 3) == 5

def test_subtract():
    assert calculadora.subtract(5, 2) == 3

def test_multiply():
    assert calculadora.multiply(4, 5) == 20

def test_divide():
    assert calculadora.divide(10, 2) == 5
