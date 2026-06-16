# operators in python

numberOne = 10;
numberTwo = 5;


# arithmetic operators 
print(numberOne + numberTwo)
print(numberOne - numberTwo)
print(numberOne * numberTwo)
print(numberOne ** numberTwo)   # Exponent
print(numberOne / numberTwo)
print(numberOne // numberTwo)   # Floor Division
print(numberOne % numberTwo)


# comparison operators
print(numberOne > numberTwo)
print(numberOne < numberTwo)
print(numberOne <= numberTwo)
print(numberOne >= numberTwo)
print(numberOne == numberTwo)
print(numberOne != numberTwo)


# assignment operators
numberOne = 5
print(numberOne)
numberOne += 5
print(numberOne)
numberOne -= 5
print(numberOne)
numberOne *= 5
print(numberOne)
numberOne **= 2
print(numberOne)
numberOne /= 5
print(numberOne)
numberOne /= 5
print(numberOne)
numberOne %= 5
print(numberOne)


# logical operators
age = 20
print(age > 18 and age < 30)
print(age > 18 or age > 50)
print(not age > 18)


# identity operators
a = [1, 2]
b = a
c = [1, 2]
print(a is b)
print(a is c)
print(a is not c)


# membership operators
colors = ["Red", "Blue", "Green"]
print("Red" in colors)
print("Blue" in colors)
print("Blue" not in colors)


# bitwise operators
a = 5   # 0101
b = 3   # 0011
print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)
