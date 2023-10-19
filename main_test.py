import pytest
from main import czy_n_pierwsza, liczby_pierwsze_do_n


def test_czy_pierwsza_dla_liczby_2():
    assert czy_n_pierwsza(2) == True


def test_czy_pierwsza_dla_liczby_3():
    assert czy_n_pierwsza(3) == True


def test_czy_pierwsza_dla_liczby_4():
    assert czy_n_pierwsza(4) == False


def test_czy_pierwsza_dla_liczby_17():
    assert czy_n_pierwsza(17) == True


def test_czy_pierwsza_dla_25():
    assert czy_n_pierwsza(25) == False


def test_czy_pierwsza_dla_liczby_ujemnej():
    assert czy_n_pierwsza(-5) == False


def test_czy_pierwsza_dla_0():
    assert czy_n_pierwsza(0) == False


def test_czy_pierwsza_dla_97():
    assert czy_n_pierwsza(97) == True


def test_czy_pierwsza_dla_100():
    assert czy_n_pierwsza(100) == False


def test_czy_pierwsza_dla_97_razy_97():
    assert czy_n_pierwsza(97 * 97) == False


def test_liczby_pierwsze_do_n_dla_n_rowne_1():
    result = liczby_pierwsze_do_n(1)
    assert result == []


def test_liczby_pierwsze_do_n_dla_n_rowne_2():
    result = liczby_pierwsze_do_n(2)
    assert result == [2]


def test_liczby_pierwsze_do_n_dla_n_rowne_10():
    result = liczby_pierwsze_do_n(10)
    assert result == [2, 3, 5, 7]


def test_liczby_pierwsze_do_n_dla_n_rowne_20():
    result = liczby_pierwsze_do_n(20)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19]


def test_liczby_pierwsze_do_n_dla_n_rowne_ujemnej():
    result = liczby_pierwsze_do_n(-5)
    assert result == []


def test_liczby_pierwsze_do_n_dla_n_rowne_100():
    result = liczby_pierwsze_do_n(100)
    assert result == [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]
