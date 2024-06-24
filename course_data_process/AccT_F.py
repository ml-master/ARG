import math

# 给定的 F1real 和 F1fake 值
F1real = 0.921
F1fake = 0.645

# 给定的 accuracy
accuracy = 0.870

# 计算 Precision 和 Recall
def calculate_precision_recall(F1):
    P = R = math.sqrt(F1 / (2 - F1))
    return P, R

Preal, Rreal = calculate_precision_recall(F1real)
Pfake, Rfake = calculate_precision_recall(F1fake)

# 假设正类和负类的样本数
Nreal = 301
Nfake = 343

# 计算 TP, FN, TN, FP
TP = Preal * Nreal
FN = Nreal - TP
TN = Pfake * Nfake
FP = Nfake - TN

# 计算 precision
precision1 = TP / (TP + FN)
precision2 = TN / (TN + FP)
print(f"Precision: {precision1:.4f}, {precision2:.4f}")

