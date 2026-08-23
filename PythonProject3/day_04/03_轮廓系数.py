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

sse, my_score = [], []

for cluster_num in range(2,15):
    kmeans = KMeans(n_clusters=cluster_num, random_state=42)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)
    y_pred = kmeans.predict(X)
    my_score.append(silhouette_score(X, y_pred))

plt.plot(range(2,15), sse, marker='o')
plt.title('Elbow Method')
plt.show()

plt.plot(range(2,15), my_score, marker='o')
plt.title('Silhouette Score')
plt.show()

