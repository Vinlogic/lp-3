import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("sales_data_sample.csv", encoding="cp1252")

# Select Sales and Quantity columns only
X = data[["SALES", "QUANTITYORDERED"]]

if len(X) < 3:
    print("Not enough data for clustering")
    exit()

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
print(data[["ORDERNUMBER", "SALES", "QUANTITYORDERED", "Cluster"]].head())

print("\nCluster Count:")
print(data["Cluster"].value_counts().sort_index())

# Plot clusters
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=data["Cluster"]
)

plt.xlabel("Sales (scaled)")
plt.ylabel("Quantity Ordered (scaled)")
plt.title("Sales Data Clustering")
plt.show()
