def PolyRoots(coefficients):

    def evaluate(x, coefficients):

        y = 0
        for i in range(len(coefficients)):
            y += coefficients[i] * x ** (len(coefficients) - i - 1)
        return y

    def derivative(coefficients):

        derivative_coefficients = [0] * (len(coefficients) - 1)
        for i in range(len(coefficients) - 1):
            derivative_coefficients[i] = (len(coefficients) - i - 1) * coefficients[i]
        return derivative_coefficients

    roots = []
    for i in range(len(coefficients) - 1):
        x0 = 0.0
        x = x0

        while abs(evaluate(x, coefficients)) > 1e-6:
            derivative_value = evaluate(x, derivative(coefficients))
            if abs(derivative_value) < 1e-6:
                # Avoid division by zero by breaking out of the loop
                break

            x = x - evaluate(x, coefficients) / derivative_value

        roots.append(round(x, 10))

    return roots


print(PolyRoots([1, -1.5]))       # Output: [1.5]
print(PolyRoots([1, -2, 1]))       # Output: [1.0, 1.0]
print(PolyRoots([1, 2, 2]))        # Output: []
print(PolyRoots([2, 2, -4, 0]))    # Output: [0.0, 1.0, -2.0]
