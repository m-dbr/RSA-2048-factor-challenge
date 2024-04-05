def factorize_number(number):
    factors = []
    divisor = 2
    while number > 1:
        print(f"Checking %: {divisor}")
        while number % divisor == 0:
            factors.append(divisor)
            print(f"---------Found factor: {divisor}")
            number //= divisor
        divisor += 1
    return factors

def main():
    # Open the file and read the numbers
    with open("number.txt", "r") as file:
        numbers = file.readlines()

    # Remove newline characters
    numbers = [int(number.strip()) for number in numbers]

    # Factorize each number and print the result
    for number in numbers:
        print(f"Factors of {number}: {factorize_number(number)}")

if __name__ == "__main__":
    main()
