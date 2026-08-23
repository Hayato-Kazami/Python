"""
集成学习 (Ensemble Learning) 教学代码
讲解 Bagging 和 Boosting 两种主要方法
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("集成学习 (Ensemble Learning) 教学演示")
print("=" * 60)

# ==================== 1. 生成数据集 ====================
print("\n【1】生成分类数据集...")
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15,
                            n_redundant=5, random_state=42, n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"训练集大小: {X_train.shape[0]}, 测试集大小: {X_test.shape[0]}")

# ==================== 2. 基学习器: 单层决策树 ====================
print("\n【2】基学习器 (单层决策树) 性能:")
base_tree = DecisionTreeClassifier(max_depth=3, random_state=42)
base_tree.fit(X_train, y_train)
base_pred = base_tree.predict(X_test)
base_acc = accuracy_score(y_test, base_pred)
print(f"  准确率: {base_acc:.4f}")

# ==================== 3. Bagging - 随机森林 ====================
print("\n" + "=" * 60)
print("【3】Bagging 方法 - 随机森林 (Random Forest)")
print("=" * 60)
print("""
Bagging 原理:
- 从训练集中有放回地采样多个Bootstrap子集
- 每个子集并行训练一个基学习器
- 预测时进行投票(分类)或平均(回归)
- 关键: 并行训练 + 降低方差
""")

rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
print(f"随机森林准确率: {rf_acc:.4f}")
print(f"相比基学习器提升: {(rf_acc - base_acc)*100:.2f}%")

# 随机森林特征重要性
print("\n特征重要性 (前5个):")
importances = rf.feature_importances_
top_5_idx = np.argsort(importances)[-5:][::-1]
for i, idx in enumerate(top_5_idx):
    print(f"  特征 {idx}: {importances[idx]:.4f}")

# ==================== 4. Boosting - AdaBoost ====================
print("\n" + "=" * 60)
print("【4】Boosting 方法 - AdaBoost")
print("=" * 60)
print("""
AdaBoost 原理:
- 串行训练多个弱学习器
- 每轮增加分错样本的权重
- 最终加权投票，准确率高者权重更大
- 关键: 串行训练 + 降低偏差
""")

adaboost = AdaBoostClassifier(n_estimators=50, learning_rate=1.0, random_state=42)
adaboost.fit(X_train, y_train)
ada_pred = adaboost.predict(X_test)
ada_acc = accuracy_score(y_test, ada_pred)
print(f"AdaBoost 准确率: {ada_acc:.4f}")
print(f"相比基学习器提升: {(ada_acc - base_acc)*100:.2f}%")

# ==================== 5. Boosting - Gradient Boosting ====================
print("\n" + "=" * 60)
print("【5】Boosting 方法 - Gradient Boosting")
print("=" * 60)
print("""
Gradient Boosting 原理:
- 每个新学习器拟合前一个学习器的残差(负梯度)
- 类似梯度下降，逐步优化损失函数
- XGBoost/LightGBM 是其优化版本
""")

gbdt = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, 
                                   max_depth=3, random_state=42)
gbdt.fit(X_train, y_train)
gbdt_pred = gbdt.predict(X_test)
gbdt_acc = accuracy_score(y_test, gbdt_pred)
print(f"Gradient Boosting 准确率: {gbdt_acc:.4f}")
print(f"相比基学习器提升: {(gbdt_acc - base_acc)*100:.2f}%")

# ==================== 6. 结果对比 ====================
print("\n" + "=" * 60)
print("【6】方法对比总结")
print("=" * 60)

methods = ['基决策树', '随机森林(Bagging)', 'AdaBoost', 'Gradient Boosting']
accuracies = [base_acc, rf_acc, ada_acc, gbdt_acc]

for method, acc in zip(methods, accuracies):
    print(f"  {method:20s}: {acc:.4f}")

print("\n【核心区别】")
print("""
  Bagging (随机森林):
  - 并行训练，采样Bootstrap子集
  - 降低方差，防止过拟合
  - 适合高方差模型(深决策树)
  
  Boosting (AdaBoost/GBDT):
  - 串行训练，关注困难样本
  - 降低偏差，提升拟合能力
  - 适合高偏差模型(浅决策树)
""")

# ==================== 7. 可视化 ====================
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 准确率对比柱状图
ax1 = axes[0, 0]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
bars = ax1.bar(methods, accuracies, color=colors)
ax1.set_ylim(0.5, 1.0)
ax1.set_title('模型准确率对比')
for bar, acc in zip(bars, accuracies):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             f'{acc:.4f}', ha='center', fontsize=9)

# 随机森林 - 学习曲线
ax2 = axes[0, 1]
n_estimators_range = range(10, 201, 10)
rf_scores = []
for n in n_estimators_range:
    rf_temp = RandomForestClassifier(n_estimators=n, max_depth=5, random_state=42)
    rf_temp.fit(X_train, y_train)
    rf_scores.append(accuracy_score(y_test, rf_temp.predict(X_test)))
ax2.plot(n_estimators_range, rf_scores, 'b-o', markersize=3)
ax2.set_title('随机森林: 树数量 vs 准确率')
ax2.set_xlabel('树的数量')
ax2.set_ylabel('准确率')
ax2.grid(True, alpha=0.3)

# AdaBoost - 学习曲线
ax3 = axes[1, 0]
ada_scores = []
for n in n_estimators_range:
    ada_temp = AdaBoostClassifier(n_estimators=n, learning_rate=1.0, random_state=42)
    ada_temp.fit(X_train, y_train)
    ada_scores.append(accuracy_score(y_test, ada_temp.predict(X_test)))
ax3.plot(n_estimators_range, ada_scores, 'r-o', markersize=3)
ax3.set_title('AdaBoost: 迭代次数 vs 准确率')
ax3.set_xlabel('迭代次数')
ax3.set_ylabel('准确率')
ax3.grid(True, alpha=0.3)

# Bagging vs Boosting 对比
ax4 = axes[1, 1]
bagging_scores = [base_acc] + rf_scores[::2][:9]
boosting_scores = [base_acc] + ada_scores[::2][:9]
x = range(10)
ax4.plot(x, bagging_scores, 's-', label='Bagging (RF)', linewidth=2)
ax4.plot(x, boosting_scores, 'o-', label='Boosting (AdaBoost)', linewidth=2)
ax4.set_title('Bagging vs Boosting 收敛对比')
ax4.set_xlabel('迭代步数')
ax4.set_ylabel('准确率')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('D:/Code/PythonProject2/day_02/ensemble_comparison.png', dpi=150, bbox_inches='tight')
print("\n【可视化】已保存: ensemble_comparison.png")
plt.show()

print("\n集成学习教学演示完成!")
