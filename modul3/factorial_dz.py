def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    

def number_of_groups(n, k):
    return int(factorial(n)/(factorial(n - k) * factorial(k)))



a = number_of_groups(5, 3)
print(a)
