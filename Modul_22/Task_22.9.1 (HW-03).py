array = input('Enter numbers separated by spaces: ')
array = array.split()
def check_num(s): # проверка что s это число
    try:
        float(s)
        return True
    except ValueError:
        return False

if all(check_num(s) for s in array): # проверка что все введенные данные это числа
    array = [float(num) for num in array] # создание списка
    print("All entered values are numbers.")
else:
    print("The entered string contains more than just numbers. Check the entered data")
    exit()

def sort(array): # сортировка пузырьком
    for i in range(len(array)):
        for j in range(len(array) -i -1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

sort(array)
print(array)

input_num = input('Enter number: ')

def check_num(s): # проверка что s это число
    try:
        float(s)
        return True
    except ValueError:
        return False

if check_num(input_num): # проверка что введено число
    input_num = float(input_num)
    print("Entered value is numbers.")
else:
    print("The entered string contains more than just numbers. Check the entered data")
    exit()

def search(array, input_num):
    left = 0
    right = len(array)
    while left < right:
        middle = (left + right) // 2

        if array[middle] < input_num:
            left = middle + 1
        else:
            right = middle

    return left - 1 if 0 < left < len(array) else "The number is not included in the list"
# возвращает индекс элемента меньше input_num
# если индекс left - 1 больше 0 и меньше len(array), то все хорошо
# если это условие не выполняется, введенное число не входит в массив array

result = search(array,input_num)
print(result)