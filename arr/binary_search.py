num_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19,
           20, 21, 22, 23, 24, 25, 26, 27, 28,
           29, 30, 31, 32, 33, 34, 35, 36, 37,
           38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

# Работает только по отсортированному типу данных

# бинарным поиском стр 27
def binary_search(ar, item):
    low = 0
    high = len(ar)-1
    o_big = 0
    while low <= high:
        o_big += 1
        mid = (low + high) // 2  # деление по модулю чтоб не создовать float
        gees = ar[mid]
        if gees == item:
            return f'Элемент {mid} кол. оп {o_big}'
        if gees > item:
            high = mid - 1
        else:
            low = mid + 1
    return f'Элемент {None} кол. оп {o_big}'


if __name__ == '__main__':
    print(binary_search(num_arr, 155))

