
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("uber.csv")

# Select required columns
data = data[[
    "fare_amount",
    "pickup_longitude",
    "pickup_latitude",
    "dropoff_longitude",
    "dropoff_latitude",
    "passenger_count"
]].dropna()

# Remove invalid values
data = data[
    (data["fare_amount"] > 0) &
    (data["passenger_count"] > 0)
]

# Calculate distance using Haversine formula
lat1 = np.radians(data["pickup_latitude"])
lat2 = np.radians(data["dropoff_latitude"])
lon1 = np.radians(data["pickup_longitude"])
lon2 = np.radians(data["dropoff_longitude"])

a = (
    np.sin((lat2 - lat1) / 2) ** 2 +
    np.cos(lat1) * np.cos(lat2) *
    np.sin((lon2 - lon1) / 2) ** 2
)

data["distance"] = 6371 * 2 * np.arcsin(
    np.sqrt(np.clip(a, 0, 1))
)

# Remove zero-distance rides
data = data[data["distance"] > 0]

# Input and output
X = data[["distance", "passenger_count"]]
y = data["fare_amount"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict fares
predictions = model.predict(X_test)

# Evaluate model
print("MAE:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Predict new ride fare
distance = float(input("Enter distance in km: "))
passengers = int(input("Enter passengers: "))

new_ride = pd.DataFrame(
    [[distance, passengers]],
    columns=["distance", "passenger_count"]
)

fare = model.predict(new_ride)[0]

print("Predicted Uber Fare:", round(max(0, fare), 2))


# -----------------------------------------
# SAMPLE INPUT:
# Dataset: uber.csv
# Enter distance in km: 10
# Enter passengers: 2
#
# SAMPLE OUTPUT:
# MAE: (Calculated from dataset)
# R2 Score: (Calculated from dataset)
# Predicted Uber Fare: (Predicted value)
#
# INSTALL LIBRARIES:
# python -m pip install pandas numpy scikit-learn
#
# RUN:
# python P6.py
# -----------------------------------------
