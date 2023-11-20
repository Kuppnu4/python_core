def fibonacci(n):
    if n == 1:
        return 1
    elif n < 1:
        return 0
    
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

a = fibonacci(int(input()))
print(a)
