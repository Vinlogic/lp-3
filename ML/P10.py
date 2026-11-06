
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("sample.csv", encoding="cp1252")

# Select Sales and Profit columns only
X = data[["Sales", "Profit"]]

if len(X) < 3 or X.shape[1] == 0:
    raise ValueError("Not enough numerical data for clustering")

# Fill missing values
X = X.fillna(X.median())

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)

# Perform clustering
data["Cluster"] = model.fit_predict(X_scaled)

# Display results
print("Clustered Sales Data:")
print(data.head())

print("\nCluster Count:")
print(data["Cluster"].value_counts().sort_index())

# Plot clusters
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1] if X_scaled.shape[1] > 1
    else [0] * len(X_scaled),
    c=data["Cluster"]
)

plt.xlabel(X.columns[0])
plt.ylabel(X.columns[1] if X.shape[1] > 1 else "Cluster view")
plt.title("Sales Data Clustering")
plt.show()


# -----------------------------------------
# SAMPLE INPUT:
# Dataset: sample.csv
# Numerical columns: Sales, Profit
#
# SAMPLE OUTPUT:
# Clustered Sales Data:
# (First five records with cluster labels)
#
# Cluster Count:
# 0    (Number of records)
# 1    (Number of records)
# 2    (Number of records)
#
# INSTALL:
# python -m pip install pandas matplotlib scikit-learn
#
# RUN:
# python P10.py
# -----------------------------------------
