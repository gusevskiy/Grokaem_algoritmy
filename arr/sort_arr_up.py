

num_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19,
           20, 21, 22, 23, 24, 25, 26, 27, 28,
           29, 30, 31, 32, 33, 34, 35, 36, 37,
           38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

offset_arr = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
              20, 21, 22, 23, 24, 25, 26, 27, 28,
              29, 30, 31, 32, 33, 34, 35, 36, 37,
              38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
              0, 1, 2, 3, 4, 5, 6, 7, 8]



# create_num_arr = list(range(50))
# print(num_arr)




# сортировка выбором | не работает
def selctionSort(ar):
    new_arr = []
    for i in range(len(ar)):
        smalles = find_smalles(ar)
        new_arr.append(smalles)
    return new_arr





if __name__ == '__main__':
    print(find_smalles(offset_arr))

    #print(selctionSort(offset_arr))