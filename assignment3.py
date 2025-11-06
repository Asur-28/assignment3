# 3. task 1 

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"Factorial of {num} is: {factorial(num)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")




# 3 task 2 


import math

def calculate_math_operations():
    try:
        num = float(input("Enter a number: "))
        if num <= 0:
            print("Logarithm is not defined for zero or negative numbers.")
        else:
            print(f"Square root: {math.sqrt(num)}")
            print(f"Logarithm: {math.log(num)}")
        print(f"Sine: {math.sin(num)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    calculate_math_operations()
