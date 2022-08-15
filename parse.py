import sys
from typing import Union, List, Optional
import re

AST = Union[str, int, List['AST']]


def tokenize(s: str) -> Optional[List[str]]:
    return re.findall(r'[()]|[^\s()]+', s)


def parse(tokens: List[str]) -> AST:
    outer_scope = []
    scope_stack = [outer_scope]
    for t in tokens:
        if t == '(':
            new_scope = []
            if scope_stack:
                scope_stack[-1].append(new_scope)
            scope_stack.append(new_scope)
        elif t == ')':
            scope_stack.pop()
        elif t.isnumeric():
            scope_stack[-1].append(int(t))
        else:
            scope_stack[-1].append(t)

    return outer_scope[0]


def ast(s: str) -> Optional[AST]:
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
