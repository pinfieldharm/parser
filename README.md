# Simple Lisp Parser

Take in a simplified lisp and print out an AST.

## Usage

To use, supply a filename with some code in it, ast is printed out.

```
$ python parse.py example.lisp 
['first', ['list', 1, ['+', 2, 3], 9]]
```

## Tests

Some unit tests are provided which require pytest.

## Notes

This was tested with python 3.10, but should work with earlier versions.