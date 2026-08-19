def power(p, n):
    if n == 0:
        return 1
    else:
        return p * power(p, n - 1)

p = int(input("Enter principal:"))
n = int(input("Enter number of years:"))

result = power(p, n)
print("Power =", result)
