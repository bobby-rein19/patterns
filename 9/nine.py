def pattern9(N):
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()


N = int(input("please enter the number:"))
pattern9(N)
