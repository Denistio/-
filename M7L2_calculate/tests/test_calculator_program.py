import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_subtraction():
    assert calculate(5, 3, '-') == 2

def test_calculate_multiplication():
    assert calculate(3, 3, '*') == 9

def test_calculate_division():
    assert calculate(4, 2, '/') == 2

def test_nool():
    assert calculate(5, 0, '/') == "Ошибка: Деление на ноль."
def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."
