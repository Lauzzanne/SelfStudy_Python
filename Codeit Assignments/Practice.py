# Linear Search

def linear_search(element, some_list):
    result = None
    for i in range(len(some_list)):
        if element == some_list[i]:
            result = i
    return result


print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))