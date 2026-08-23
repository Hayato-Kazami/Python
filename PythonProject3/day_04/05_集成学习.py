"""
集成学习 (Ensemble Learning) 教学示例
集成学习通过组合多个基学习器来提高预测性能
主要方法：Bagging, Boosting, Stacking
"""

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import (
    RandomForestClassifier,      # Bagging - 随机森林
    AdaBoostClassifier,          # Boosting - AdaBoost
    GradientBoostingClassifier,  # Boosting - GBDT
    VotingClassifier,            # Voting - 投票集成
    StackingClassifier           # Stacking - 堆叠集成
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# 加载数据集（鸢尾花数据集）
iris = datasets.load_iris()
X, y = iris.data, iris.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print("=" * 60)
print("集成学习示例 - 鸢尾花分类")
print("=" * 60)

# ==================== 1. 单个决策树（基学习器）====================
print("\n--- 1. 单个决策树 ---")
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
dt_acc = accuracy_score(y_test, dt_pred)
print(f"准确率: {dt_acc:.4f}")

# ==================== 2. Bagging - 随机森林 ====================
print("\n--- 2. Bagging - 随机森林 ---")
print("原理：并行训练多个决策树，每棵树使用不同的数据采样和特征子集")
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
print(f"准确率: {rf_acc:.4f}")

# ==================== 3. Boosting - AdaBoost ====================
print("\n--- 3. Boosting - AdaBoost ---")
print("原理：串行训练，每棵树关注之前分错的样本")
ada = AdaBoostClassifier(n_estimators=100, random_state=42)
ada.fit(X_train, y_train)
ada_pred = ada.predict(X_test)
ada_acc = accuracy_score(y_test, ada_pred)
print(f"准确率: {ada_acc:.4f}")

# ==================== 4. Boosting - GBDT ====================
print("\n--- 4. Boosting - GBDT (Gradient Boosting) ---")
print("原理：每棵树拟合前面模型的残差（梯度）")
gbdt = GradientBoostingClassifier(n_estimators=100, random_state=42)
gbdt.fit(X_train, y_train)
gbdt_pred = gbdt.predict(X_test)
gbdt_acc = accuracy_score(y_test, gbdt_pred)
print(f"准确率: {gbdt_acc:.4f}")

# ==================== 5. Voting - 软投票集成 ====================
print("\n--- 5. Voting - 软投票集成 ---")
print("原理：结合不同模型的预测概率，取加权平均")
voting = VotingClassifier(
    estimators=[
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
        ('svc', SVC(probability=True, random_state=42)),
        ('knn', KNeighborsClassifier(n_neighbors=3))
    ],
    voting='soft'  # 软投票（基于概率）
)
voting.fit(X_train, y_train)
voting_pred = voting.predict(X_test)
voting_acc = accuracy_score(y_test, voting_pred)
print(f"准确率: {voting_acc:.4f}")

# ==================== 6. Stacking - 堆叠集成 ====================
print("\n--- 6. Stacking - 堆叠集成 ---")
print("原理：用基学习器的预测作为新特征，训练元学习器")
stacking = StackingClassifier(
    estimators=[
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
        ('gbdt', GradientBoostingClassifier(n_estimators=100, random_state=42)),
        ('knn', KNeighborsClassifier(n_neighbors=3))
    ],
    final_estimator=LogisticRegression(),  # 元学习器
    cv=5  # 5折交叉验证
)
stacking.fit(X_train, y_train)
stacking_pred = stacking.predict(X_test)
stacking_acc = accuracy_score(y_test, stacking_pred)
print(f"准确率: {stacking_acc:.4f}")

# ==================== 结果对比 ====================
print("\n" + "=" * 60)
print("结果对比")
print("=" * 60)
results = {
    '单个决策树': dt_acc,
    '随机森林 (Bagging)': rf_acc,
    'AdaBoost (Boosting)': ada_acc,
    'GBDT (Boosting)': gbdt_acc,
    'Voting 集成': voting_acc,
    'Stacking 集成': stacking_acc
}

for name, acc in results.items():
    print(f"  {name:20s}: {acc:.4f}")

best = max(results, key=results.get)
print(f"\n最佳方法: {best} ({results[best]:.4f})")

# ==================== 特征重要性 ====================
print("\n--- 随机森林特征重要性 ---")
for i, importance in enumerate(rf.feature_importances_):
    print(f"  特征 {i}: {importance:.4f}")