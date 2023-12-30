# Напишите функцию find_median, которая будет возвращать
# одно число - медианное значение.
# Если переданный в функцию список окажется пустым - верните None.
# Функция find_median принимает на вход
# arr - исходный список с числами.

arr = [100, 5, 2, 4, 3, 6]
arr.sort()
def find_median(arr):
    n = len(arr)
    if n == 0:
        return None
    elif n % 2 == 0:
        median = (arr[n//2] + arr[n//2 - 1]) / 2 # деление с дробной частью
        return median
    else:
        n % 2 ==1
        median = arr[n//2] # цельночисленное деление, дробная часть отбрасывается
        return median

print(arr)
print(find_median(arr))


