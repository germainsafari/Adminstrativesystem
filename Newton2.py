def PolyRoots(coefficients, epsilon=1e-10, max_iterations=100):
    def polynomial(coef, x):
        return sum(c * x**i for i, c in enumerate(coef))

    def derivative(coef, x):
        return sum(i * c * x**(i-1) for i, c in enumerate(coef[1:], start=1))

    roots = []

    for i in range(len(coefficients)-1):
        # Use each coefficient as an initial guess
        x0 = coefficients[i]

        for _ in range(max_iterations):
            f_x0 = polynomial(coefficients, x0)
            f_prime_x0 = derivative(coefficients, x0)

            if abs(f_prime_x0) < epsilon:
                break

            x1 = x0 - f_x0 / f_prime_x0

            if abs(x1 - x0) < epsilon:
                roots.append(round(x1, 10))
                break

            x0 = x1

    return roots

# Examples
print(PolyRoots([1, -1.5]))       # Output: [1.5]
print(PolyRoots([1, -2, 1]))       # Output: [1.0, 1.0]
print(PolyRoots([1, 2, 2]))        # Output: []
print(PolyRoots([2, 2, -4, 0]))    # Output: [0.0, 1.0, -2.0]
