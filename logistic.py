import numpy as np
import matplotlib.pyplot as plt

# Sigmoid function
def sigmoid(z):
    """
    Compute the sigmoid of z.
    """
    return 1 / (1 + np.exp(-z))

# Binary Cross-Entropy Loss
def cross_entropy_loss(y_true, y_pred):
    """
    Compute binary cross-entropy loss.
    """
    epsilon = 1e-15  # To avoid log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# Gradient Descent
def gradient_descent(X, y, weights, learning_rate, iterations):
    """
    Perform gradient descent to optimize weights.
    """
    m = X.shape[0]
    for i in range(iterations):
        predictions = sigmoid(np.dot(X, weights))
        errors = predictions - y
        gradient = np.dot(X.T, errors) / m
        weights -= learning_rate * gradient

        if i % 100 == 0:
            loss = cross_entropy_loss(y, predictions)
            print(f"Iteration {i}: Loss = {loss:.4f}")

    return weights

# Predict using the sigmoid function
def predict(X, weights):
    """
    Predict using sigmoid function.
    """
    probabilities = sigmoid(np.dot(X, weights))
    return (probabilities >= 0.5).astype(int)

# Logistic Regression Model
def logistic_regression(X, y, learning_rate=0.01, iterations=1000):
    """
    Fit logistic regression model.
    """
    X = np.hstack((np.ones((X.shape[0], 1)), X))  # Add bias term
    weights = np.zeros(X.shape[1])
    weights = gradient_descent(X, y, weights, learning_rate, iterations)
    return weights

# Evaluate accuracy
def evaluate(y_true, y_pred):
    """
    Compute accuracy.
    """
    accuracy = np.mean(y_true == y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    return accuracy

# Data Preprocessing
# Dataset from the lab document
X = np.array([
    [0.1, 1.1],
    [1.2, 0.9],
    [1.5, 1.6],
    [2.0, 1.8],
    [2.5, 2.1],
    [0.5, 1.5],
    [1.8, 2.3],
    [0.2, 0.7],
    [1.9, 1.4],
    [0.8, 0.6]
])
y = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 0])

# Normalize the dataset
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_normalized = (X - X_mean) / X_std

# Visualize the data points
plt.scatter(X_normalized[y == 0, 0], X_normalized[y == 0, 1], color='red', label='Class 0')
plt.scatter(X_normalized[y == 1, 0], X_normalized[y == 1, 1], color='blue', label='Class 1')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.title("Data Distribution")
plt.show()

# Train the model
weights = logistic_regression(X_normalized, y, learning_rate=0.1, iterations=1000)

# Predict and evaluate
X_with_bias = np.hstack((np.ones((X_normalized.shape[0], 1)), X_normalized))
y_pred = predict(X_with_bias, weights)
evaluate(y, y_pred)

# Visualize Decision Boundary
def plot_decision_boundary(X, y, weights):
    """
    Plot the decision boundary.
    """
    x_values = np.array([min(X[:, 0]), max(X[:, 0])])
    y_values = -(weights[0] + weights[1] * x_values) / weights[2]

    plt.scatter(X[y == 0, 0], X[y == 0, 1], color='red', label='Class 0')
    plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue', label='Class 1')
    plt.plot(x_values, y_values, label='Decision Boundary', color='green')
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.title("Decision Boundary")
    plt.show()

plot_decision_boundary(X_normalized, y, weights)