
import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = np.array([
    [0.1, 0.6],
    [0.15, 0.71],
    [0.25, 0.8],
    [0.35, 0.45],
    [0.5, 0.5],
    [0.6, 0.2],
    [0.65, 0.3],
    [0.8, 0.35]
])
y = np.array([1, 1, 1, 1, 0, 0, 0, 0])  # Labels

# Step 2: Initialize weights and biases
def initialize_parameters(input_size, hidden_size, output_size):
    weights = {
        "W1": np.random.randn(input_size, hidden_size) * 0.01,
        "b1": np.zeros((1, hidden_size)),
        "W2": np.random.randn(hidden_size, output_size) * 0.01,
        "b2": np.zeros((1, output_size))
    }
    return weights

# Step 3: Forward propagation
def forward_propagation(X, weights):
    Z1 = np.dot(X, weights["W1"]) + weights["b1"]
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, weights["W2"]) + weights["b2"]
    A2 = 1 / (1 + np.exp(-Z2))  # Sigmoid activation
    cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}
    return A2, cache

# Step 4: Compute binary cross-entropy loss
def compute_loss(y_true, y_pred):
    m = y_true.shape[0]
    loss = -np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)) / m
    return loss

# Step 5: Backward propagation
def backward_propagation(X, y, weights, cache):
    m = X.shape[0]
    A1, A2 = cache["A1"], cache["A2"]
    dZ2 = A2 - y.reshape(-1, 1)
    dW2 = np.dot(A1.T, dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m
    dZ1 = np.dot(dZ2, weights["W2"].T) * (1 - np.power(A1, 2))
    dW1 = np.dot(X.T, dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m
    gradients = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}
    return gradients

# Step 6: Update parameters
def update_parameters(weights, gradients, learning_rate):
    for key in weights:
        weights[key] -= learning_rate * gradients["d" + key]
    return weights

# Step 7: Training loop
def train_network(X, y, hidden_size, learning_rate, epochs):
    np.random.seed(42)
    input_size, output_size = X.shape[1], 1
    weights = initialize_parameters(input_size, hidden_size, output_size)
    losses = []

    for epoch in range(epochs):
        y_pred, cache = forward_propagation(X, weights)
        loss = compute_loss(y, y_pred)
        losses.append(loss)
        gradients = backward_propagation(X, y, weights, cache)
        weights = update_parameters(weights, gradients, learning_rate)
        
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

    return weights, losses

# Step 8: Plot decision boundary
def plot_decision_boundary(X, y, weights):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    grid = np.c_[xx.ravel(), yy.ravel()]
    _, cache = forward_propagation(grid, weights)
    predictions = (cache["A2"] > 0.5).reshape(xx.shape)
    
    plt.contourf(xx, yy, predictions, alpha=0.8, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors="k", cmap=plt.cm.Spectral)
    plt.show()

# Hyperparameters
hidden_size = 3
learning_rate = 0.1
epochs = 1000

# Train the network
trained_weights, loss_history = train_network(X, y, hidden_size, learning_rate, epochs)

# Visualize the decision boundary
plot_decision_boundary(X, y, trained_weights)
