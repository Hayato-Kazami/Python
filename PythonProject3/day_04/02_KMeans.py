from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import calinski_harabasz_score
import matplotlib.pyplot as plt

# 生成模拟数据
X, _ = make_blobs(n_samples=100, n_features=2, centers=[[0,0],[2,2],[3,3],[4,4]],
                  cluster_std=[0.3,0.2,0.5,0.4], random_state=15)

print(f"原始数据：{X}")
print(len(X))
plt.figure()
plt.scatter(X[:,0], X[:,1])
plt.show()


# 使用KMeans进行聚类
kmeans = KMeans(n_clusters=4, random_state=15)
y_pred = kmeans.fit_predict(X)
print(f"聚类结果：{y_pred}")

# 计算聚类质量指标
ch_score = calinski_harabasz_score(X, y_pred)
print(f"聚类质量指标：{ch_score}")

# 可视化聚类结果
plt.figure()
plt.scatter(X[:,0], X[:,1], c=y_pred)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker='x', color='red')
plt.show()