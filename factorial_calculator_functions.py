def get_non_negative_integer() -> int:
    """
    Prompt the user to enter a non-negative integer and validate the input.
    
    Returns:
        int: The validated non-negative integer.
    """
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))
            if number < 0:
                print("Error: Please enter a non-negative integer.")
            else:
                return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a given non-negative integer.
    
    Args:
        n (int): The non-negative integer.
    
    Returns:
        int: The calculated factorial.
    """
    if n == 0:
        return 1
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# Main Program Flow
if __name__ == "__main__":
    user_number = get_non_negative_integer()
    result = calculate_factorial(user_number)
    print(f"The factorial of {user_number} is: {result}")