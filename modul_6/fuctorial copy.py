def fuctorial(n):
    if n == 1:
        return 1
    else:
        return n * fuctorial(n-1)

x = input("input a number < 10: ")
print(f"fuctorial {x}: " + fuctorial(x))
