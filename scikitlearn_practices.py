import sklearn as skl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Advertising.csv")
df["total_spend"] = df["TV"] + df["radio"] + df["newspaper"]
print(df.head())
# create the scatterplot
# sns.scatterplot(data=df, x="total_spend", y="sales",)
# create a linear model on the plot
# sns.regplot(data=df,x="total_spend", y="sales")
# show the plot
# plt.show()
X = df["total_spend"]
y = df["sales"]
# y=B1X+B0
print(np.polyfit(X, y, 1))
potential_spend = np.linspace(0, 500, 100)
predicted_sales = potential_spend * 0.04868788 + 4.24302822
# plt.plot(potential_spend,predicted_sales)
# plt.show()

OP_TYPES = [
    "Seq Scan",
    "Index Scan",
    "Bitmap Index Scan",
    "Bitmap Heap Scan",
    "Nested Loop",
    "Hash Join",
    "Merge Join",
    "Aggregate",
    "Sort",
    "Limit",
    "Gather",
]
# op_name = input("Enter your Operator: ")
# vector = [0] * len(OP_TYPES)
# if op_name in OP_TYPES:
# idx = OP_TYPES.index(op_name)
# vector[idx] = 1
# print(f" His Vector is: {vector}")
print([2, 3, 8] + [2, 1, 6])
arr = [0, 0,3]
arr2 = arr + np.array([8, 3]).tolist()
print(arr2)
print(type(arr2))
