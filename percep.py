# Perceptron Implementation
def perceptron(X, y, learning_rate=0.01, epochs=100):
    weights = [0] * len(X[0])  # Initialize weights to 0
    bias = 0

    for _ in range(epochs):
        for i in range(len(X)):
            activation = sum(X[i][j] * weights[j] for j in range(len(X[0]))) + bias
            prediction = 1 if activation >= 0 else 0
            update = learning_rate * (y[i] - prediction)
            weights = [weights[j] + update * X[i][j] for j in range(len(X[0]))]
            bias += update

    return weights, bias

# Visualization of Perceptron Decision Boundary
def plot_perceptron_boundary(X, y, weights, bias):
    print("\nDecision Boundary Points:")
    for x1 in range(-10, 11):  # Adjust range as needed
        x2 = -(weights[0] * x1 + bias) / weights[1] if weights[1] != 0 else 0
        print(f"x1: {x1}, x2: {x2:.2f}")
    print("\nData Points:")
    for i in range(len(X)):
        print(f"Point: {X[i]}, Label: {y[i]}")

# Example Data
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]  # Example for AND gate

weights, bias = perceptron(X, y, learning_rate=0.1, epochs=10)
plot_perceptron_boundary(X, y, weights, bias)
