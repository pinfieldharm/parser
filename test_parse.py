import pytest

from parse import ast


def test_parse_example():
    s = "(first (list 1 (+ 2 3) 9))"
    result = ast(s)
    assert result == ["first", ["list", 1, ["+", 2, 3], 9]]


def test_parse_multiple_sibling_lists():
    s = "(alpha (beta 1 2) (gamma 3 4))"
    result = ast(s)
    assert result == ["alpha", ["beta", 1, 2], ["gamma", 3, 4]]


def test_parse_empty():
    s = ""
    result = ast(s)
    assert result is None


def test_parse_empty_whitespace():
    s = "      "
    result = ast(s)
    assert result is None


def test_empty_list():
    s = "()"
    result = ast(s)
    assert result == []


def test_empty_list_embedded():
    s = "(foo ())"
    result = ast(s)
    assert result == ["foo", []]


def test_not_a_program():
    with pytest.raises(SyntaxError):
        s = "abc 1 2 3"
        ast(s)