import pytest
import main

def func(x):
    return x + 5

def test_method():
    assert func(3) == 8

def test_method2():
    assert main.test_method3(3) == 8