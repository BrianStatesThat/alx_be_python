def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1: First operand
        num2: Second operand
        operation: The operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        The result of the arithmetic operation.
        Returns "Cannot divide by zero!" for division by zero cases.
    """
    operation = operation.lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero!"
        return num1 / num2
    else:
        return "Invalid operation!"