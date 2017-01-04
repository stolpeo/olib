import pytest
from olib import olib


def test_debug_false():
    def increase(x):
        return x + 1

    assert olib.debug(active=False)(increase)(1) == 2


def test_debug_true():
    def increase(x):
        return x + 1

    assert olib.debug(active=True)(increase)(1) == 2


def test_debug_true_capsys(capsys):
    def increase(x):
        return x + 1

    olib.debug()(increase)(1)
    out, err = capsys.readouterr()

    assert out.endswith('increase(1) -> 2\n')
