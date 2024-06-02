#making a list
array = [1, 2, 3, 3, 3, 4]

#will print elements of array
for i in range(len(array)):
    print(array[i])

#function for checking target in array
def filter(array, target):
    return [x for x in array if x == target]

#function call to print array and its len
print(filter(array, 3), len(filter(array, 3)), sep = ", ")
    