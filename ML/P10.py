import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("sales_data_sample.csv", encoding="cp1252")

# Select Sales and Quantity columns only
X = data[["SALES", "QUANTITYORDERED"]]

# Fill missing values and scale data
X = X.fillna(X.median())
X_scaled = StandardScaler().fit_transform(X)

# Elbow method: find a suitable number of clusters
inertia = []
for k in range(1, 11):
    inertia.append(KMeans(n_clusters=k, random_state=42, n_init=10).fit(X_scaled).inertia_)

plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# Create K-Means model (k = 3 chosen from the elbow)
model = KMeans(n_clusters=3, random_state=42, n_init=10)

# Perform clustering
data["Cluster"] = model.fit_predict(X_scaled)

# Display results
print("Clustered Sales Data:")
print(data[["ORDERNUMBER", "SALES", "QUANTITYORDERED", "Cluster"]].head())

print("\nCluster Count:")
print(data["Cluster"].value_counts().sort_index())

# Plot clusters
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=data["Cluster"])
plt.colorbar(label="Cluster")
plt.xlabel("Sales (scaled)")
plt.ylabel("Quantity Ordered (scaled)")
plt.title("Sales Data Clustering")
plt.show()
