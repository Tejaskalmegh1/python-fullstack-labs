# conditional statements in python


# if 
age = 18
if age >= 18:
    print("You are eligible to vote")


# if else 
age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")    


# if-elif-else
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# nested if
age = 25
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("Get a driving license first")
else:
    print("You are too young to drive")    


# ternary operator
age = 20
message = "Adult" if age >= 18 else "Minor"
print(message)
