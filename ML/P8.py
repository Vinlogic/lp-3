
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

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

# Identify numerical and categorical columns
num_cols = X.select_dtypes(include="number").columns
cat_cols = X.select_dtypes(exclude="number").columns

# Preprocess the data
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
])

# Create neural network model
model = make_pipeline(
    preprocessor,
    MLPClassifier(
        hidden_layer_sizes=(16, 8),
        max_iter=500,
        random_state=42
    )
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train neural network
model.fit(X_train, y_train)

# Predict customer churn
predictions = model.predict(X_test)

# Evaluate model
print("Accuracy:", accuracy_score(y_test, predictions))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Predict one customer
result = model.predict(X_test.iloc[[0]])[0]

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
