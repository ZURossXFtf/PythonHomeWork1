 # Задача 1
print('Задача 1:')
rains = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
     11, 12, 13, 333, 15, 16, 17, 18,
     19, 20,30,22,23,24,3335,26,27,28,29)

print(str(rains.index(max(rains))) + "-ого Февраля выпало самое большое кол-во осадков\n")

 # Задача 2
print('Задача 2:')

import numpy as np

array = np.random.randint(0, 100, (5, 5))
print("Исходный массив:\n", array)

max_value = np.max(array)
max_index = np.unravel_index(np.argmax(array, axis=None), array.shape)


if max_index[0] != 0:
    array[[0, max_index[0]]] = array[[max_index[0], 0]]


if max_index[1] != 0:
    array[:, [0, max_index[1]]] = array[:, [max_index[1], 0]]

print("Массив после перемещения наибольшего элемента:\n", array)

 # Задача 3
print('Задача 3:')
my_list = [1, 2, 3, 3, 9, 6, 7, 8, 9, 10,]

unique_elements = []

for i in my_list:
    if  my_list.count(i) == 1:
        unique_elements.append(i)
print('Исходный массив: '+ str(my_list))
print('Элементы массвива встречающиеся 1 раз: '+ str(unique_elements)+'\n')

# Задача 4
print('Задача 4:')
more = set('qwertysssseeeqqqqquiop[]asdfghjklzxcvbnm/')
print(more)
print('Различных символов: '+str(len(more))+'\n')

# Задача 5
print('Задача 5:')
dictionary = {'a': 3, 'b': 6, 'c': 4}
print(dictionary)

def result_mult(input_dict):
    result = 1
    for value in input_dict.values():
         result *= value
    return result


product = result_mult(dictionary)
print("Произведение всех значений словаря:", product)
