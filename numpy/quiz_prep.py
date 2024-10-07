import numpy as np


my_list: list[int] = [1, 2, 3, 4, 5]

my_array = np.array(my_list)

print(my_array)

print(np.arange(3, 11, 3))

print(np.random.rand(2))

np.random.seed(2)
print(np.random.rand(3))

print(np.random.rand(3))

print(my_array.reshape(5,1))

bool_arr = my_array < 5
print(my_array[bool_arr])
print(my_array.mean())

print(np.linspace(0, 10, 101))

def myadd(x, y):
    return x+y

my_add = np.frompyfunc(myadd, 2, 1)

print(my_add([1,2], [1,2]))