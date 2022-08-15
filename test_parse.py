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


def test_atom_is_valid():
    s = "1234"
    result = ast(s)
    assert result == 1234


def test_wrong_parens():
    s = ") foo 1 2"
    with pytest.raises(SyntaxError, match="Unbalanced parens"):
        ast(s)


def test_dangling_parens():
    s = "( ( 1 3 2"
    with pytest.raises(SyntaxError, match="Unbalanced parens"):
        ast(s)


def test_multiple_atoms():
    s = "1 2 3 4"
    with pytest.raises(SyntaxError, match="Too many top-level expressions"):
        ast(s)


def test_negative_number():
    s = "-1"
    result = ast(s)
    assert result == -1
