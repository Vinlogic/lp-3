import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score
)

# Load dataset
data = pd.read_csv("diabetes.csv")

# Separate input and output
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Replace invalid zero values with missing values
cols = [
    "Glucose", "BloodPressure",
    "SkinThickness", "Insulin", "BMI"
]
X[cols] = X[cols].replace(0, float("nan"))

# Split dataset before filling missing values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Fill missing values using training data median only
median = X_train.median()
X_train = X_train.fillna(median)
X_test = X_test.fillna(median)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create KNN model
model = KNeighborsClassifier(n_neighbors=5)

# Train model
model.fit(X_train, y_train)

# Predict results
predictions = model.predict(X_test)

# Calculate performance
cm = confusion_matrix(y_test, predictions)
accuracy = accuracy_score(y_test, predictions)
error = 1 - accuracy
precision = precision_score(y_test, predictions, zero_division=0)
recall = recall_score(y_test, predictions, zero_division=0)

# Display results
print("Confusion Matrix:")
print(cm)
print("Accuracy:", accuracy)
print("Error Rate:", error)
print("Precision:", precision)
print("Recall:", recall)


# -----------------------------------------
# SAMPLE INPUT:
# Dataset: diabetes.csv
#
# SAMPLE OUTPUT:
# Confusion Matrix:
# [[... ...]
#  [... ...]]
# Accuracy: (Calculated value)
# Error Rate: (Calculated value)
# Precision: (Calculated value)
# Recall: (Calculated value)
#
# INSTALL:
# python -m pip install pandas scikit-learn
#
# RUN:
# python P9.py
# -----------------------------------------
