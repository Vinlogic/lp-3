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

# Remove invalid values and unusual coordinates (keep only New York area)
data = data[
    (data["fare_amount"] > 0) &
    (data["fare_amount"] <= 100) &
    (data["passenger_count"].between(1, 6)) &
    (data["pickup_latitude"].between(40, 42)) &
    (data["dropoff_latitude"].between(40, 42)) &
    (data["pickup_longitude"].between(-75, -72)) &
    (data["dropoff_longitude"].between(-75, -72))
]

# Function to calculate distance (in km) using Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1 = np.radians(lat1), np.radians(lon1)
    lat2, lon2 = np.radians(lat2), np.radians(lon2)

    a = (
        np.sin((lat2 - lat1) / 2) ** 2 +
        np.cos(lat1) * np.cos(lat2) *
        np.sin((lon2 - lon1) / 2) ** 2
    )

    return 6371 * 2 * np.arcsin(np.sqrt(np.clip(a, 0, 1)))

# Calculate distance for every ride
data["distance"] = haversine(
    data["pickup_latitude"], data["pickup_longitude"],
    data["dropoff_latitude"], data["dropoff_longitude"]
)

# Remove very short and very long rides
data = data[data["distance"].between(0.1, 50)]

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

# Predict fares for test data
predictions = model.predict(X_test)

# Evaluate model
print("MAE:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Predict new ride fare using pickup and drop-off points
pickup_lat = float(input("Enter pickup latitude: "))
pickup_lon = float(input("Enter pickup longitude: "))
dropoff_lat = float(input("Enter dropoff latitude: "))
dropoff_lon = float(input("Enter dropoff longitude: "))
passengers = int(input("Enter passengers: "))

if not (40 <= pickup_lat <= 42 and 40 <= dropoff_lat <= 42 and
        -75 <= pickup_lon <= -72 and -75 <= dropoff_lon <= -72):
    print("Invalid input: use New York coordinates (lat 40-42, lon -75 to -72)")
elif not 1 <= passengers <= 6:
    print("Invalid input: passengers must be between 1 and 6")
else:
    distance = haversine(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon)

    new_ride = pd.DataFrame(
        [[distance, passengers]],
        columns=["distance", "passenger_count"]
    )

    fare = model.predict(new_ride)[0]

    print("Distance:", round(distance, 2), "km")
    print("Predicted Uber Fare: $", round(max(0, fare), 2))

# -----------------------------------------
# SAMPLE INPUT:
# Dataset: uber.csv
# Enter pickup latitude: 40.7580
# Enter pickup longitude: -73.9855
# Enter dropoff latitude: 40.7484
# Enter dropoff longitude: -73.9857
# Enter passengers: 2
#
# SAMPLE OUTPUT:
# MAE: 2.206143968277565
# R2 Score: 0.822888982945244
# Distance: 1.07 km
# Predicted Uber Fare: $ 5.92
#
# INSTALL:
# python -m pip install pandas numpy scikit-learn
# -----------------------------------------
