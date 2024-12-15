# Step 1: Calculate Mean
def calculate_mean(values):
    """
    Calculate the mean of a list of values.
    """
    return sum(values) / len(values)

# Step 2: Calculate Slope
def calculate_slope(X, Y, mean_X, mean_Y):
    """
    Calculate the slope (theta_1) using the covariance and variance formulas.
    """
    numerator = sum((x - mean_X) * (y - mean_Y) for x, y in zip(X, Y))
    denominator = sum((x - mean_X) ** 2 for x in X)
    return numerator / denominator

# Step 3: Calculate Intercept
def calculate_intercept(mean_X, mean_Y, slope):
    """
    Calculate the intercept (theta_0).
    """
    return mean_Y - (slope * mean_X)

# Step 4: Make Predictions
def predict(X, intercept, slope):
    """
    Predict Y values based on X, intercept, and slope.
    """
    return [intercept + slope * x for x in X]

# Step 5: Calculate MSE
def calculate_mse(Y, Y_pred):
    """
    Calculate Mean Squared Error (MSE) between actual and predicted values.
    """
    return sum((y - y_pred) ** 2 for y, y_pred in zip(Y, Y_pred)) / len(Y)

# Step 6: Gradient Descent for Weight Adjustment
def gradient_descent(X, Y, intercept, slope, learning_rate, iterations):
    """
    Adjust the intercept and slope using gradient descent to minimize MSE.
    """
    n = len(X)
    for _ in range(iterations):
        Y_pred = predict(X, intercept, slope)
        # Compute gradients
        slope_gradient = -2 / n * sum(x * (y - y_pred) for x, y, y_pred in zip(X, Y, Y_pred))
        intercept_gradient = -2 / n * sum(y - y_pred for y, y_pred in zip(Y, Y_pred))
        # Update weights
        slope -= learning_rate * slope_gradient
        intercept -= learning_rate * intercept_gradient
    return intercept, slope

# Step 7: Fit Linear Regression
def fit_linear_regression(X, Y, learning_rate=0.01, iterations=1000):
    """
    Fit the linear regression model by calculating slope, intercept,
    and refining them using gradient descent.
    """
    mean_X, mean_Y = calculate_mean(X), calculate_mean(Y)
    slope = calculate_slope(X, Y, mean_X, mean_Y)
    intercept = calculate_intercept(mean_X, mean_Y, slope)
    intercept, slope = gradient_descent(X, Y, intercept, slope, learning_rate, iterations)
    return intercept, slope

# Step 8: Test the Model
def test_model():
    """
    Test the linear regression model using the provided dataset.
    """
    # Dataset
    X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Y = [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000]

    # Fit Model
    intercept, slope = fit_linear_regression(X, Y, learning_rate=0.01, iterations=1000)

    # Make Predictions
    Y_pred = predict(X, intercept, slope)

    # Evaluate Model
    mse = calculate_mse(Y, Y_pred)
    print(f"Intercept: {intercept}, Slope: {slope}")
    print(f"Mean Squared Error: {mse}")
    print(f"Predicted Values: {Y_pred}")

# Run the test
test_model()
