import pytest

from src.calculator import calculator as calc

@pytest.mark.parametrize("n, expected",
                         [pytest.param(1, 1),
                         pytest.param(3, 9),
                         pytest.param(-2, 4)])
def test_squareNums(n, expected):
    assert calc.squareNums(n) == expected 

@pytest.mark.parametrize("n, expected",
                         [pytest.param(2, 3),
                         pytest.param(3, 6),
                         pytest.param(5, 15)])
def test_truNums(n, expected):
    assert calc.triNums(n) == expected 


@pytest.mark.parametrize("n, expected",
                         [pytest.param(2, 6),
                         pytest.param(3, 15),
                         pytest.param(6, 66)])
def test_hexagonalNums(n, expected):
    assert calc.hexagonalNums(n) == expected 


@pytest.mark.parametrize("n, expected",
                         [pytest.param(1, 1),
                         pytest.param(3, 6),
                         pytest.param(4, 24)])
def test_factorial(n, expected):
    assert calc.factorial(n) == expected 


@pytest.mark.parametrize("n, expected",
                         [pytest.param(1, 1),
                         pytest.param(3, 5),
                         pytest.param(6, 132)])
def test_catalanNums(n, expected):
    assert calc.catalanNums(n) == expected 


@pytest.mark.parametrize("n, expected",
                         [pytest.param(1, 2),
                         pytest.param(3, 7),
                         pytest.param(5, 16)])
def test_lazyCaterer(n, expected):
    assert calc.lazyCaterer(n) == expected 


@pytest.mark.parametrize("n, expected",
                         [pytest.param(1, 1),
                         pytest.param(2, 5),
                         pytest.param(5, 65)])
def test_magicSquares(n, expected):
    assert calc.magicSquares(n) == expected 