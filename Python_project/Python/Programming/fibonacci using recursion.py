def fib(N):
    if N == 1 or N == 2:
        return N - 1
    return fib(N - 1) + fib(N - 2)


for x in range(1, 6):
    print(fib(x))
