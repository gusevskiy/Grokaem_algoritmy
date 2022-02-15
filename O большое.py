# О большое - подсчитывает количество операций
from random import randint

# create array
arr = []
while len(arr) < 10:
    arr.append(randint(1, 10))
print('Массив-', *arr)


# Вывод значения каждого элемента массива
def output_big_O(arr):
    big_O = 0
    for i in arr:
        big_O += 1
    return big_O


print(output_big_O(arr))

# Удвоение значения каждого элемента массива
# Удвоение значения только первого элемента массива
#
