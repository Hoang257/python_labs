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

def unique_sorted(nums: List[float|int]) -> List[float|int]:
    return sorted(set(nums)) #возвращаем отсортированный список
print("\nТест unique_sorted:")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

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

