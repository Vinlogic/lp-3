# Gradient Descent to find the local minimum of y = (x + 3)^2
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return (x + 3) ** 2

def derivative(x):                 # dy/dx = 2(x + 3)
    return 2 * (x + 3)

x = 2                              # starting point
learning_rate = 0.1                # step size
tolerance = 1e-6                   # stop when x barely changes
max_iterations = 1000              # safety limit
iteration = 0

x_history = [x]                    # store every x to draw the path later

while iteration < max_iterations:
    gradient = derivative(x)
    new_x = x - learning_rate * gradient       # main formula

    print("Iteration:", iteration + 1,
          "x =", round(new_x, 6),
          "y =", round(function(new_x), 6))

    x_history.append(new_x)

    if abs(new_x - x) < tolerance:             # converged, so stop
        x = new_x
        break

    x = new_x
    iteration += 1

print("\nLocal minimum occurs at x =", round(x, 6))
print("Minimum value of y =", round(function(x), 6))

# ---------- Plot ----------
x_values = np.linspace(-8, 4, 100)
y_values = function(x_values)

plt.plot(x_values, y_values, label="y = (x + 3)^2")
plt.scatter(2, function(2), color="green", label="Starting Point (2, 25)")
plt.scatter(x, function(x), color="red", label="Minimum Point (-3, 0)")

path_y = [function(i) for i in x_history]
plt.plot(x_history, path_y, "o--", label="Gradient Descent Path")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Gradient Descent for y = (x + 3)^2")
plt.legend()
plt.grid()
plt.show()
