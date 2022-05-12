from time import sleep


ar = [1, 4, 7, 12, 5]

# Сортировка массива
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr [1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
#print('быстрая сортировка массива ', quicksort(ar))




def print_import_slip1(list):
    for i in list:
        print(i, end=' ')


def print_import_slip2(list):
    for i in list:
        sleep(2) # задержка 2 секунды
        print(i, end=' ')



if __name__ == '__main__':
    print_import_slip1(ar)
    print()
    print_import_slip2(ar)