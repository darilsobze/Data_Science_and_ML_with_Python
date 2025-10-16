import numpy as np

array= np.arange(11)
print(array)
num= array[5]
print(num)
set_of_num= array[2:5]
print(set_of_num)
set_of_num[:]=88
print(set_of_num)
print(array)
print(array[array>5])
my_matrix = [[1,3,2],[4,9,8],[8,5,7]]
np_matrix= np.array(my_matrix)
print(my_matrix)
print(np_matrix)
slice_matrix = np_matrix[:2,1:]
print("Here is my matrix")
print(slice_matrix)