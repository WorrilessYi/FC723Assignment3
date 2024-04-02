def GCD(a, b):
    # Greatest common divisor
    if a == 0:
        # GCD(0, b) = b
        return b
    elif b == 0:
        # GCD(a, 0) = a
        return a
    else:
        # a = b * quotient + remainder
        remainder = a % b
        # call the function again
        return GCD(b, remainder)
def user_interface():
    print("Welcome to the relative prime number calculator!")
    while True:
        num1 = input("Please enter the first number: ")
        while not num1.isnumeric():
            num1 = input("Please enter valid number: ")
        num1 = int(num1)
        num2 = input("Please enter the second number: ")
        while not num2.isnumeric():
            num2 = input("Please enter valid number: ")
        num2 = int(num2)
        common_divisor = GCD(num1, num2)
        if common_divisor == 1:
            print(f"{num1} and {num2} are relative primes, the GCD is {common_divisor}")
        elif GCD(num1, num2) == -1:
            print(f"{num1} and {num2} are relative primes")
        else:
            print(f"{num1} and {num2} are not relative primes")
        ask = input("Do you want to calculate again?(no): ")
        if ask.lower() == "no":
            break
    print("Thanks for using this calculator")


user_interface()
