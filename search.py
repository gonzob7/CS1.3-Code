

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if array[index] == item:
        return index
    elif index == len(array) - 1:
        return None

    return linear_search_recursive(array, item, index + 1)

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0
    right = len(array)
    found = False

    while not found:
        middle = (right - left) // 2 + left #calculates current mid point
        pointer = array[middle]

        if pointer == item:
            found = True
        elif middle == left or middle == right: #checks if we have reached the end
            return None
        elif pointer > item: #if item is greater than the current middle
            right = middle
        elif pointer < item: #if item is less than the current middle
            left = middle

    return middle


def binary_search_recursive(array, item, left=None, right=None):

    # TODO: implement binary search recursively here

    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1

    middle = ((right - left) // 2) + left #calculates current mid point
    pointer = array[middle] #active pointer

    if pointer == item:
        return middle
    elif middle == left or middle == right: #checks if we have reached the end
        return None
    elif pointer > item: #if item is greater than the current middle
        return binary_search_recursive(array, item, left, middle - 1)
    elif pointer < item: #if item is less than the current middle
        return binary_search_recursive(array, item, middle + 1, right)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
