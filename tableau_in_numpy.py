import numpy as np
# List in Python
my_list= [1,2,6,8,9]
print(my_list)
print(type(list))

# Arrays with numpy
np_array = np.array(my_list)
print(np_array)
print(type(np_array))

array2= np.arange(12)
print(array2)
print(np.arange(5,20))
print(np.random.randint(0,50,(5,2)))