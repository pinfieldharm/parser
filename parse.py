from typing import Union, List, Optional
import re

AST = Union[str, List['AST']]


def tokenize(s: str) -> Optional[List[str]]:
    return re.findall(r'[()]|[^\s()]+', s)


def parse(tokens: List[str]) -> AST:
    scopes = []
    last_scope = None
    for t in tokens:
        if t == '(':
            new_scope = []
            if scopes:
                scopes[-1].append(new_scope)
            scopes.append(new_scope)
        elif t == ')':
            last_scope = scopes.pop()
        elif t.isnumeric():
            scopes[-1].append(int(t))
        else:
            scopes[-1].append(t)

    return last_scope


def ast(s: str) -> Optional[AST]:
    tokens = tokenize(s)
    if not tokens:
        return None
    return parse(tokens)


if __name__ == '__main__':
    print("Write me!")
