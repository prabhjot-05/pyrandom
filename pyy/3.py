def rec(n):
    if n==1 or n==0:
        return 1
    return n*rec(n-1)

print(rec(5))

print("Welcome")
