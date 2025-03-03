#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
#Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.
#Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.
#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.


def prog1():
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))
    print(f"The bigger number is {max(num1, num2)}.")


def prog2():
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))
    if num1 == num2:
        print("Numbers entered are equal.")
    else:
        print(f"The bigger number is {max(num1, num2)}.")


def prog3():
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))
    print(f"The sum is {num1 + num2}.")


def prog4():
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))
    print(f"The product is {num1 * num2}.")


def prog5():
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))
    print(f"The quotient is {num1 / num2:.2f}.")


def prog6():
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))
    print(f"The result is {num1 ** num2}.")


def prog7():
    total = sum(float(input(f"Enter number {i + 1}: ")) for i in range(10))
    print(f"The sum of all 10 numbers is: {total}.")


def prog8():
    odd_count = sum(1 for i in range(10) if float(input(f"Enter number {i + 1}: ")) % 2 != 0)
    print(f"The count of odd numbers is: {odd_count}.")


def prog9():
    print("Even numbers from 0 to 100:")
    for num in range(0, 101, 2):
        print(num)


def prog10():
    print("Numbers from 0 to 100 except those ending in zero:")
    for num in range(101):
        if num % 10 != 0:
            print(num)


while True:
    print("Welcome.")
    print("\nChoose a program:")
    for i in range(1, 11):
        print(f"{i}. Prog{i}")
    print("11. Exit")
    choice = input("Enter your choice (1-11): ")

    if choice == "1":
        prog1()
    elif choice == "2":
        prog2()
    elif choice == "3":
        prog3()
    elif choice == "4":
        prog4()
    elif choice == "5":
        prog5()
    elif choice == "6":
        prog6()
    elif choice == "7":
        prog7()
    elif choice == "8":
        prog8()
    elif choice == "9":
        prog9()
    elif choice == "10":
        prog10()
    elif choice == "11":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 11.")

