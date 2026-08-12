def countdown(n):
    if n == 0:
        print("Launch")
    else:
        print(n)
        countdown(n - 1)

n = int(input("Enter countdown number:"))

countdown(n)
