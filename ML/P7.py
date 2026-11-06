
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("spam.csv", encoding="latin-1")

# Select required columns
data = data[["v1", "v2"]].dropna()
data.columns = ["label", "email"]

# Convert labels into numbers
data["label"] = data["label"].str.lower().map({
    "ham": 0,
    "spam": 1
})

data = data.dropna()

X = data["email"]
y = data["label"].astype(int)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create KNN model
knn = make_pipeline(
    TfidfVectorizer(),
    KNeighborsClassifier(n_neighbors=5)
)

# Create SVM model
svm = make_pipeline(
    TfidfVectorizer(),
    LinearSVC()
)

# Train models
knn.fit(X_train, y_train)
svm.fit(X_train, y_train)

# Make predictions
knn_pred = knn.predict(X_test)
svm_pred = svm.predict(X_test)

# Compare performance
print("\nKNN Performance")
print("Accuracy:", accuracy_score(y_test, knn_pred))
print(classification_report(
    y_test, knn_pred,
    target_names=["Normal", "Spam"],
    zero_division=0
))

print("\nSVM Performance")
print("Accuracy:", accuracy_score(y_test, svm_pred))
print(classification_report(
    y_test, svm_pred,
    target_names=["Normal", "Spam"],
    zero_division=0
))

# Predict a new email using SVM
email = input("Enter an email message: ")

result = svm.predict([email])[0]

if result == 1:
    print("Spam Email")
else:
    print("Normal Email")


# -----------------------------------------
# SAMPLE INPUT:
# Dataset: spam.csv
# Enter an email message:
# Congratulations! You have won a free prize.
#
# SAMPLE OUTPUT:
# KNN Performance
# Accuracy: (Calculated value)
#
# SVM Performance
# Accuracy: (Calculated value)
#
# Enter an email message:
# Congratulations! You have won a free prize.
# Spam Email
#
# INSTALL:
# python -m pip install pandas scikit-learn
#
# RUN:
# python P7.py
# -----------------------------------------
