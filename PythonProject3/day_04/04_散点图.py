import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('./data/customers.csv')
print(data.head())
data.info()

# 提取特征
X = data.iloc[:,[3,4]]

kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)
y_pred = kmeans.predict(X)
print(y_pred)
print(X.values.shape)
print(y_pred == 0)
print(X.values[y_pred == 0,1])
print(kmeans.cluster_centers_)

plt.scatter(X.values[y_pred == 0,0], X.values[y_pred == 0,1], c='red', s = 100, label='Cluster 1')
plt.scatter(X.values[y_pred == 1,0], X.values[y_pred == 1,1], c='blue', s = 100, label='Cluster 2')
plt.scatter(X.values[y_pred == 2,0], X.values[y_pred == 2,1], c='green', s = 100, label='Cluster 3')
plt.scatter(X.values[y_pred == 3,0], X.values[y_pred == 3,1], c='purple', s = 100, label='Cluster 4')
plt.scatter(X.values[y_pred == 4,0], X.values[y_pred == 4,1], c='orange', s = 100, label='Cluster 5')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], c='black', s = 300, label='Centroids')
plt.legend()
plt.xlabel('Income')
plt.ylabel('Spending')
plt.show()
