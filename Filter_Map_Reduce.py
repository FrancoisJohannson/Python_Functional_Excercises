from functools import reduce
from typing import List

list_X: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# get all uneven numbers
filter_object = filter(lambda it: it % 2, list_X)
print(list(filter_object))

# square every element
map_object = map(lambda it: it * it, list_X)
print(list(map_object))

# the sum of all elements
reduce_result = reduce(lambda accumulator, it: accumulator + it, list_X)
print(reduce_result)
