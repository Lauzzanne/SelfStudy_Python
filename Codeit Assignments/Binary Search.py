def binary_search(element, some_list):
    first_index = 0
    end_index = len(some_list) - 1
    while first_index <= end_index:
        mid_index = (first_index + end_index) // 2
        if element == some_list[mid_index]:
            return mid_index
        elif element > some_list[mid_index]:
            first_index = mid_index + 1
        else:
            end_index = mid_index - 1



print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))