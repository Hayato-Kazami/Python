from sklearn.metrics import confusion_matrix, f1_score, recall_score
import pandas as pd

y_true = ["恶性","恶性","恶性","恶性","恶性","恶性","良性","良性","良性","良性"]
lables = ["恶性","良性"]
df_name = ["恶性(正例)","良性(负例)"]

y_predA = ["良性","恶性","恶性","恶性","良性","良性","良性","良性","良性","良性"]

matrix = confusion_matrix(y_true, y_predA, labels=lables)
print(pd.DataFrame(matrix, index=df_name, columns=df_name))

y_predB = ["恶性","良性","良性","良性","良性","良性","良性","良性","良性","良性"]
matrixB = confusion_matrix(y_true, y_predB, labels=lables)
print(pd.DataFrame(matrixB, index=df_name, columns=df_name))

precisionA = recall_score(y_true, y_predA, pos_label="恶性")
print("召回率A:",precisionA)

precisionB = recall_score(y_true, y_predB, pos_label="恶性")
print("召回率B:",precisionB)

f1_A = f1_score(y_true, y_predA, pos_label="恶性")
print("F1分数A:",f1_A)

f1_B = f1_score(y_true, y_predB, pos_label="恶性")
print("F1分数B:",f1_B)