def print1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

n = int(input("enter number"))
print1(n)