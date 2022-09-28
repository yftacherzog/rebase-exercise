#!/usr/bin/env python3

def foo(foo: str) -> str:
    return f"Foo:{foo.upper()}_{foo.lower()}"

if __name__ == "__main__":
    print(foo("bar"))
