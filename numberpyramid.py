#to create a pyramid of numbers from 1 to 20 using for loop
n = 1
for i in range(1,21):
    for j in range(1, i + 1):
        print(n,end=" ")
        n = n + 1
        while n == 21:
            exit()
    print("\n")







