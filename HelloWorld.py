#Simple calculator in Python with **KapFresh**

#Enter first number
num1 = int(input("Please enter number 1 \n"))

#Enter second number
num2 = int(input("Please input number 2 \n"))

#then ask the user to choose an option
ans = input("Choose option: \n a) Addition \n b) Subtraction \n c) Muliplication \n d) Division \n")

#if statment

#Addition
if ans == "a":  
    print(num1 + num2)

#Subtraction
if ans == "b":
    print(num1 - num2)

#Muliplication
if ans =="c":
    print(num1 * num2)

#Division
if ans =="d":
    print(num1 / num2)
