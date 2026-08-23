from sklearn.metrics import confusion_matrix
import pandas as pd

# 生成混淆矩阵
y_true = ["恶性","恶性","恶性","恶性","恶性","恶性","良性","良性","良性","良性"]
lables = ["恶性","良性"]
df_name = ["恶性(正例)","良性(负例)"]

y_predA = ["良性","恶性","恶性","恶性","良性","良性","良性","良性","良性","良性"]

matrix = confusion_matrix(y_true, y_predA, labels=lables)
print(pd.DataFrame(matrix, index=df_name, columns=df_name))

y_predB = ["恶性","恶性","恶性","恶性","恶性","恶性","良性","良性","良性","良性"]
matrixB = confusion_matrix(y_true, y_predB, labels=lables)
print(pd.DataFrame(matrixB, index=df_name, columns=df_name))