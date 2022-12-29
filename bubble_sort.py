offset_arr = [90, 11, 40, 167, 19]

# for i in range(len(offset_arr)-1):
#     print(offset_arr[i])
def bubblesort(array):
    length = len(array)
    for i in range(length-1):
        for x in range(length-1-i):
            # если соседний элемент меньше
            if array[x+1] < array[x]:
                # меняем их местами (можно через множ присваивание a,b=b,a)
                temporary = array[x]
                array[x] = array[x+1]
                array[x+1] = temporary
    return array

print(bubblesort(offset_arr))