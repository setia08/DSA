from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n > 0:
        return n * fibonacci(n - 1)
    return 1


feb=fibonacci(500)
print(feb)