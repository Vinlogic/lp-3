import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = pd.read_csv("Churn_Modelling.csv")

# Show first 5 rows of the dataset
print(data.head())

# Remove unnecessary columns
data = data.drop(
    columns=["RowNumber", "CustomerId", "Surname"],
    errors="ignore"
)

# Separate input and output (Exited: 1 = left, 0 = stayed)
X = data.drop("Exited", axis=1)
y = data["Exited"]

# Convert categorical columns into numbers
X = pd.get_dummies(X, columns=["Geography", "Gender"], dtype=int)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create neural network model
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    max_iter=500,
    random_state=42
)

# Train neural network
model.fit(X_train, y_train)

# Predict customer churn
predictions = model.predict(X_test)

# Evaluate model
print("\nAccuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Predict one customer (first customer of the test set)
result = model.predict(X_test[[0]])[0]

print("Prediction:", "Will LEAVE the bank" if result == 1 else "Will STAY in the bank",
      "| Actual:", "Left" if y_test.iloc[0] == 1 else "Stayed")


# -----------------------------------------
# SAMPLE INPUT:
# Dataset: Churn_Modelling.csv
#
# SAMPLE OUTPUT:
# Accuracy: 0.861
#
# Confusion Matrix:
# [[1523   70]
#  [ 208  199]]
#
# Classification Report:
#               precision    recall  f1-score   support
#            0       0.88      0.96      0.92      1593
#            1       0.74      0.49      0.59       407
#
# Prediction: Will STAY in the bank | Actual: Stayed
#
# INSTALL:
# python -m pip install pandas scikit-learn
#
# RUN:
# python P8.py
# -----------------------------------------
