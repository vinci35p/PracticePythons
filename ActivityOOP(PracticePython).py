# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
# Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.
# Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.
# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
# Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

def prog1():
    num1 = (input("Enter your 1st number: "))
    num2 = (input("Enter your 2nd number: "))

    if num1 > num2:
        print(f"The bigger number is {num1}.")

    else:
        print(f"The bigger number is {num2}")

    print("Thank you.")

def prog2():
    num1 = (input("Enter your 1st number: "))
    num2 = (input("Enter your 2nd number: "))

    if num1 > num2:
        print(f"The bigger number is {num1}.")

    elif num1 == num2:
        print("Numbers entered are equal.")

    else:
        print(f"The bigger number is {num2}")

    print("Thank you.")

def prog3():
    num1 = int((input("Enter your 1st number: ")))
    num2 = int((input("Enter your 2nd number: ")))
    num3 = num1 + num2
    print(f"The sum is {num3}.")

    print("Thank you.")

def prog4():
    num1 = int((input("Enter your 1st number: ")))
    num2 = int((input("Enter your 2nd number: ")))
    num3 = num1 * num2

    print(f"The product is {num3}.")

    print("Thank you.")

def prog5():
    num1 = int((input("Enter your 1st number: ")))
    num2 = int((input("Enter your 2nd number: ")))
    num3 = float(num1 / num2)

    print(f"The product is {num3:.2f}.")

    print("Thank you.")

def prog6():
    num1 = int((input("Enter your 1st number: ")))
    num2 = int((input("Enter your 2nd number: ")))
    num3 = float(num1 **num2)

    print(f"The product is {num3:.2f}.")

    print("Thank you.")

def prog7():
    num3 = 0

    print("Enter 10 numbers:")
    for i in range(10):
        num = float(input(f"Num {i + 1}: "))
        num3 += num

    print(f"The sum of all 10 numbers is: {num3}")

def prog8():
    num_odd = 0

    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input(f"Number {i + 1}: "))
        if num % 2 != 0:
            num_odd += 1

    print(f"The count of odd numbers is: {num_odd}")

def prog9():
    print("Even numbers from 1 to 100:")
    for num in range(2, 101, 2):
        print(num)

prog9()