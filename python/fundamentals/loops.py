# loops in python


# for loop
for i in range(1,5):
    print(i)


# while loop
i = 1
while i <= 5:
    print("hello..")
    i += 1


# star pattern using for
for i in range(1,6):
    for j in range(1,i):
        print("*", end=" ")
    print("")


# star pattern using while
i = 5
while i >= 1:
    j = 5
    while j >= i:
        print("*", end="")
        j -= 1
    print("")
    i -= 1