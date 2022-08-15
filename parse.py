from typing import Union, List, Optional
import re

AST = Union[str, List['AST']]


def tokenize(s: str) -> Optional[List[str]]:
    return re.findall(r'[()]|[^\s()]+', s)


def parse(tokens: List[str]) -> AST:
    if tokens[0] != '(' or tokens[-1] != ')':
        raise SyntaxError("Expected parens")

    scopes = [[]]
    for t in tokens[1:-1]:
        if t == '(':
            new_scope = []
            scopes[-1].append(new_scope)
            scopes.append(new_scope)
        elif t == ')':
            scopes.pop()
        elif t.isnumeric():
            scopes[-1].append(int(t))
        else:
            scopes[-1].append(t)

    return scopes[0]


def ast(s: str) -> Optional[AST]:
    tokens = tokenize(s)
    if not tokens:
        return None
    return parse(tokens)


if __name__ == '__main__':
    print("Write me!")
