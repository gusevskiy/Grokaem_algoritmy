from random import randint



ar = [1, 4, 7, 12, 5]

# for i in range(10):
#     print(i)

'''
# рекурсивная ф-я
def recurs_sum(ar):
    if not ar:
        return 0
    return ar[0] + recurs_sum(ar[1:])
print('Сумма по recurs_sum-', recurs_sum(ar))
'''

# Найти наибольший элемент в списке
a = 0
for i in ar:
    if i > a:
        a = i
print(a)
