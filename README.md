# Лабораторная работа №1

##  Задание 1
![Результат задания 1](/images/image-0.png)

##  Задание 2
![Результат задания 2](/images/image-1.png)

##  Задание 3
![Результат задания 3](/images/image-2.png)

##  Задание 4
![Результат задания 4](/images/image-3.png)

##  Задание 5
![Результат задания 5](/images/image-4.png)

##  Задание 6
![Результат задания 6](/images/image-5.png)

##  Задание 7
![Результат задания 7](/images/image-6.png)

# Лабораторная работа №2

##  Задание 1.1
```python
from typing import Union, List, Tuple 
def min_max(nums: List[Union[float, int]]) -> Tuple[Union[float, int]]:
    if not nums:
        return ('ValueError')
    return min(nums), max(nums)
print('\nТест min_max: ')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
```
![Результат задания 1.1](/images/image-8.png)

##  Задание 1.2
```python
def unique_sorted(nums: List[float|int]) -> List[float|int]:
    return sorted(set(nums)) #возвразем отсортированный список
print("\nТест unique_sorted:")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
![Результат задания 1.2](/images/image-10.png)
```
##  Задание 1.3
```python
def flatten(mat: List[List|Tuple]) -> List:
    result = [] 
    for element in mat:
        if not isinstance(element, (list, tuple)): #проверка на тип даных
            return ('TypeError')
        result.extend(element)
    return result
print("\nТест flatten:")
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1, 2], "ab"]))
```
![Результат задания 1.3](/images/image-12.png)

##  Задание 2.1
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
        return []
    num_cols = len(mat[0]) #длина столбиков
    if any(len(row) != num_cols for row in mat):
        return ('ValueError')
    return [[mat[i][j] for i in range(len(mat))] for j in range(num_cols)]
print('\nТест transpose:')
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
```
![Результат задания 2.1](/images/image-12.png)
