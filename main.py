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

def error_message():
    print("Please enter a positive integer!!")
def user_interface():
    print("Welcome to the relative prime number calculator!")
    while True:
        while True:
            num1 = input("num1: ")
            try:
                num1 = int(num1)
            except ValueError:
                error_message()
            else:
                if num1 >= 0:
                    break
                else:
                    error_message()
        while True:
            num2 = input("num2: ")
            try:
                num2 = int(num2)
            except ValueError:
                error_message()
            else:
                if num2 >= 0:
                    break
                else:
                    error_message()
        common_divisor = GCD(num1, num2)
        if common_divisor == 1:
            print(f"{num1} and {num2} are relative primes, the GCD is {common_divisor}")
        elif GCD(num1, num2) == -1:
            print(f"{num1} and {num2} are relative primes")
        else:
            print(f"{num1} and {num2} are not relative primes")
        ask = input("\nDo you want to calculate again?(no): ")
        if ask.lower() == "no":
            break
    print("Thanks for using this calculator")


user_interface()
