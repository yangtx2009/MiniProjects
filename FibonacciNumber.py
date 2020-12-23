# fib(n) = fib(n-1) + fib(n-2)
# fib(0) = fib(1) = 1

def fib(n):
    if n > 1:
        buffer = [0, 1]
        for i in range(2, n + 1):
            buffer[i % 2] = buffer[0] + buffer[1]
        return buffer[n % 2]
    else:
        return n % 2