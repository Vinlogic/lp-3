import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("uber.csv")

# Show first 5 rows of the dataset
print(data.head())

# Select required columns and remove missing values
data = data[[
    "fare_amount", "pickup_longitude", "pickup_latitude",
    "dropoff_longitude", "dropoff_latitude", "passenger_count"
]].dropna()

# Visualization 1: outliers in fare (before cleaning)
sns.boxplot(x=data["fare_amount"])
plt.title("Fare amount (before removing outliers)")
plt.show()

# Remove invalid data (New York coordinates)
data = data[
    (data["fare_amount"] > 0) &
    (data["fare_amount"] <= 100) &
    (data["passenger_count"].between(1, 6)) &
    (data["pickup_latitude"].between(40, 42)) &
    (data["dropoff_latitude"].between(40, 42)) &
    (data["pickup_longitude"].between(-75, -72)) &
    (data["dropoff_longitude"].between(-75, -72))
]

# Calculate distance using Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    a = (np.sin((lat2 - lat1) / 2) ** 2 +
         np.cos(lat1) * np.cos(lat2) *
         np.sin((lon2 - lon1) / 2) ** 2)

    return 6371 * 2 * np.arcsin(np.sqrt(np.clip(a, 0, 1)))

# Calculate ride distance
data["distance"] = haversine(
    data["pickup_latitude"], data["pickup_longitude"],
    data["dropoff_latitude"], data["dropoff_longitude"]
)

# Remove unusual distances
data = data[data["distance"].between(0.1, 50)]

# Visualization 2: correlation between columns
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation")
plt.show()

# Input and output
X = data[["distance", "passenger_count"]]
y = data["fare_amount"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Visualization 3: actual vs predicted fare (first 500 test rides)
plt.scatter(y_test[:500], predictions[:500], s=10)
plt.plot([0, 60], [0, 60], color="red")
plt.xlabel("Actual fare")
plt.ylabel("Predicted fare")
plt.title("Actual vs Predicted Fare")
plt.show()

# Take new ride details
print("\nEnter ride details:")
pickup_lat = float(input("Pickup latitude: "))
pickup_lon = float(input("Pickup longitude: "))
dropoff_lat = float(input("Dropoff latitude: "))
dropoff_lon = float(input("Dropoff longitude: "))
passengers = int(input("Number of passengers: "))

# Validate input
if not (40 <= pickup_lat <= 42 and 40 <= dropoff_lat <= 42 and
        -75 <= pickup_lon <= -72 and -75 <= dropoff_lon <= -72):
    print("Invalid New York coordinates")

elif not (1 <= passengers <= 6):
    print("Invalid passenger count")

else:
    distance = haversine(
        pickup_lat, pickup_lon, dropoff_lat, dropoff_lon
    )

    ride = pd.DataFrame(
        [[distance, passengers]],
        columns=["distance", "passenger_count"]
    )

    fare = model.predict(ride)[0]

    print("Distance:", round(distance, 2), "km")
    print("Predicted Uber Fare: $", round(max(0, fare), 2))

# -----------------------------------------
# SAMPLE INPUT:
# Dataset: uber.csv
# Pickup latitude: 40.7580
# Pickup longitude: -73.9855
# Dropoff latitude: 40.7484
# Dropoff longitude: -73.9857
# Number of passengers: 2
#
# SAMPLE OUTPUT:
# MAE: 2.2061
# R2 Score: 0.8229
# Distance: 1.07 km
# Predicted Uber Fare: $ 5.92
# (plus 3 plots: fare boxplot, correlation heatmap, actual vs predicted)
#
# INSTALL:
# python -m pip install pandas numpy scikit-learn matplotlib seaborn
#
# RUN:
# python P6.py
# -----------------------------------------
