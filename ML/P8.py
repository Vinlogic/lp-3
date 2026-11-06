import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = pd.read_csv("Churn_Modelling.csv")

# Remove unnecessary columns
data = data.drop(
    columns=["RowNumber", "CustomerId", "Surname"],
    errors="ignore"
)

# Separate input and output
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
print("Accuracy:", accuracy_score(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions, zero_division=0))

# Predict one customer
result = model.predict(X_test[[0]])[0]

if result == 1:
    print("Customer will leave the bank")
else:
    print("Customer will stay in the bank")


# -----------------------------------------
# SAMPLE INPUT:
# Dataset: Churn_Modelling.csv
#
# SAMPLE OUTPUT:
# Accuracy: (Calculated value)
# Confusion Matrix:
# [[... ...]
#  [... ...]]
# Customer prediction: (Stay or Leave)
#
# INSTALL:
# python -m pip install pandas scikit-learn
#
# RUN:
# python P8.py
# -----------------------------------------
