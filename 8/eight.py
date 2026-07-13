def pattern8(N):
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


N = int(input("please enter the number:"))
pattern8(N)
