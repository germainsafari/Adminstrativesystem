def PolyRoots(coefficients):
    # Initialize an empty list to store the roots
    roots = []


    if len(coefficients) == 0:
        return roots


    guess = 1

    # Iterate until the tolerance is reached or the maximum number of iterations is exceeded
    tolerance = 1e-6
    max_iterations = 1000
    iterations = 0
    while iterations < max_iterations:

        derivative = []
        for i in range(len(coefficients) - 1):
            derivative.append(coefficients[i] * (len(coefficients) - i - 1))


        polynomial_value = 0
        derivative_value = 0
        for i in range(len(coefficients)):
            polynomial_value += coefficients[i] * guess ** (len(coefficients) - i - 1)
            derivative_value += derivative[i] * guess ** (len(derivative) - i - 1)

        guess -= polynomial_value / derivative_value


        if abs(polynomial_value) < tolerance:
            roots.append(guess)
            break

        iterations += 1

    return roots
print(PolyRoots([1, -1.5]))       # Output: [1.5]
print(PolyRoots([1, -2, 1]))       # Output: [1.0, 1.0]
print(PolyRoots([1, 2, 2]))        # Output: []
print(PolyRoots([2, 2, -4, 0]))    # Output: [0.0, 1.0, -2.0]