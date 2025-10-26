import numpy as np
import pandas as pd

# print(help(pd.Series))

my_data = [1776, 1552, 4488]
my_index = ["USA", "CAMEROON", "MEXICO"]

my_ser = pd.Series(my_data, my_index)
print(my_ser)
print(my_ser["CAMEROON"])
print(my_ser.keys())
