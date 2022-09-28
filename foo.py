#!/usr/bin/env python3

def foo(foo: str) -> str:
    return f"foo:{foo.lower()}"

if __name__ == "__main__":
    print(foo("bar"))
