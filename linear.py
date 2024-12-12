X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 7, 8]

def calculate_mean(values):
    return sum(values) / len(values)

def calculate_slope(X, Y, mean_X, mean_Y):
    return sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X))) / sum((X[i] - mean_X) ** 2 for i in range(len(X)))

def calculate_intercept(mean_X, mean_Y, slope):
    return mean_Y - slope * mean_X

def predict(X, theta_0, theta_1):
    return [theta_0 + theta_1 * x for x in X]

def calculate_mse(Y, Y_pred):
    return sum((Y[i] - Y_pred[i]) ** 2 for i in range(len(Y))) / len(Y)

mean_X = calculate_mean(X)
mean_Y = calculate_mean(Y)
slope = calculate_slope(X, Y, mean_X, mean_Y)
intercept = calculate_intercept(mean_X, mean_Y, slope)
Y_pred = predict(X, intercept, slope)
mse = calculate_mse(Y, Y_pred)

print("\nLinear Regression Results:")
print("X:", X)
print("Y:", Y)
print("Intercept (θ₀):", intercept)
print("Slope (θ₁):", slope)
print("Predicted Y:", Y_pred)
print("Mean Squared Error (MSE):", mse)
