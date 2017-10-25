# List / Arrays
array = ['Ralph', 'Cachero']
print(array[0] + " " + array[1])

groceryArray = ['eggs', 'milk', 'cheese', 'kombucha', 'coffee', 'alligator jerky']
listSlice = groceryArray[3:5]
slice_up_to_3 = groceryArray[:3]
slice_from_3_on = groceryArray[3:]
slice_second_from_end = groceryArray[-2]

print(listSlice)
print(slice_up_to_3)
print(slice_from_3_on)
print(slice_second_from_end)

# Tuples
(x_values, y_values) = ([1, 2, 3], [-1, -2 ,-3])
print('Plot this point: ', x_values[2], ", ", y_values[0])

tuple = (x_values, y_values)
print(tuple[0][1])
