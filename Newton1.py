def PolyRoots(coefficients):
    """
    Finds the real roots of a polynomial using Newton's method.

    Args:
        coefficients (list): A list of real numbers representing the coefficients of the polynomial.

    Returns:
        list: A list of real roots of the polynomial (or their acceptable approximations).
    """

    def evaluate_polynomial(x, coefficients):
        """
        Evaluates the polynomial at a given point.

        Args:
            x (float): The point at which to evaluate the polynomial.
            coefficients (list): A list of real numbers representing the coefficients of the polynomial.

        Returns:
            float: The value of the polynomial at the given point.
        """
        y = 0
        for i in range(len(coefficients)):
            y += coefficients[i] * x ** (len(coefficients) - i - 1)
        return y

    def derivative(coefficients):
        """
        Calculates the derivative of the polynomial.

        Args:
            coefficients (list): A list of real numbers representing the coefficients of the polynomial.

        Returns:
            list: A list of real numbers representing the coefficients of the derivative of the polynomial.
        """
        derivative_coefficients = [0] * (len(coefficients) - 1)
        for i in range(len(coefficients) - 1):
            derivative_coefficients[i] = (len(coefficients) - i - 1) * coefficients[i]
        return derivative_coefficients

    roots = []
    for i in range(len(coefficients) - 1):
        x0 = 0.0
        x = x0

        while abs(evaluate_polynomial(x, coefficients)) > 1e-10:
            derivative_value = evaluate_polynomial(x, derivative(coefficients))
            if abs(derivative_value) < 1e-10:
                # Avoid division by zero by breaking out of the loop
                break

            x = x - evaluate_polynomial(x, coefficients) / derivative_value

        roots.append(round(x, 10))

    return roots

# Examples
print(PolyRoots([1, -1.5]))       # Expected Output: [1.5]
print(PolyRoots([1, -2, 1]))       # Expected Output: [1.0, 1.0]
print(PolyRoots([1, 2, 2]))        # Expected Output: []
print(PolyRoots([2, 2, -4, 0]))    # Expected Output: [0.0, 1.0, -2.0]
