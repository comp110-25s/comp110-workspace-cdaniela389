def summit(n: int) -> int:
    if n < 0:
        return -1
    elif n <= 1:
        return 0
    elif n % 2 == 1:
        return summit(n=n - 1)
    else:
        return n + summit(n=n - 2)
