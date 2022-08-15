import sys
from typing import Union, List, Optional
import re

# An AST for a simplified lisp. Strings, ints and lists.
AST = Union[str, int, List['AST']]


def tokenize(input_string: str) -> Optional[List[str]]:
    # Split up into left parens, right parens and other non-whitespace
    return re.findall(r'[()]|[^\s()]+', input_string)


def parse(tokens: List[str]) -> AST:
    # Top-level scope, should only end up with one expression in it.
    root_scope = []

    # Current chain of nested scopes. End of the list is current scope.
    scopes = [root_scope]

    for t in tokens:
        if t == '(':
            # Starting a new parenthesized section.
            new_scope = []
            scopes[-1].append(new_scope)
            scopes.append(new_scope)
        elif t == ')':
            # Ending a parenthesized section.
            if len(scopes) == 1:
                # Prevent exiting the root scope (i.e. no corresponding left paren)
                raise SyntaxError("Unbalanced parens")
            scopes.pop()
        else:
            # Adding an atom. Try to coerce into int if possible
            try:
                scopes[-1].append(int(t))
            except ValueError:
                scopes[-1].append(t)

    if len(root_scope) > 1:
        # This happens if we have too many expressions, e.g. a list of atoms
        raise SyntaxError("Too many top-level expressions")

    if len(scopes) > 1:
        # This happens if there are unclosed parentheses.
        raise SyntaxError("Unbalanced parens")

    # Return contents of root scope.
    return root_scope[0]


def ast(s: str) -> Optional[AST]:
    # Tokenize input and parse.
    tokens = tokenize(s)
    if not tokens:
        return None
    return parse(tokens)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please supply a filename")
        exit(-1)

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        s = file.read()
    print(ast(s))
