from Euclidean import EuclideanAlgorithm
eu = EuclideanAlgorithm()


def get_input():
    # Input validation loop
    while True:
        try:
            inp = input("Enter the numbers: ")
            n1, n2 = inp.split(",")
            n1 = int(n1)
            n2 = int(n2)
            if n1 <= 0 or n2 <= 0:
                raise ValueError("Input must be positive integers!")
            return n1, n2
        except ValueError as e:
            print("Invalid input:", e)


def user_interface():
    print("Welcome to the relative prime number calculator!")
    while True:
        num1, num2 = get_input()
        # Calling the greatest common divisor function
        common_divisor = eu.gcd(num1, num2)
        # Check if both numbers are 0
        if num1 == 0 and num2 == 0:
            print("Both numbers are 0. GCD is undefined.")
        # Check if GCD is 1 for relative primes
        elif common_divisor == 1:
            print(f"{num1} and {num2} are relative primes, the GCD is {common_divisor}")
        else:
            print(f"{num1} and {num2} are not relative primes, the GCD is {common_divisor}")
        # Ask user if they want to calculate again
        ask = input("\nDo you want to calculate again?(yes): ")
        # Exit loop if answer is not "yes" or "y"
        if ask.lower() != "yes" and ask.lower() != "y":
            break


# Run the user interface
user_interface()
