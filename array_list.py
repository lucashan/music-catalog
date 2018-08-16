# a ArrayList represents an array


class List:
    def __init__(self, data, length, capacity):
        self.data = data          # a list
        self.length = length      # a Int
        self.capacity = capacity  # a Int

    def __eq__(self, other):
        return (type(other) == List
                and self.data == other.data
                and self.length == other.length
                and self.capacity == other.capacity)

    def __repr__(self):
        return ("List({!r}, {!r}, {!r})"
                .format(self.data, self.length, self.capacity))


# -> List
# returns an empty list
def empty_list():
    return List([None], 0, 1)


# list int value -> ArrayList
# returns resulting list after value is placed at index position
def add(array_list, index, value):
    if index < 0 or index > array_list.length:
        raise IndexError()
    else:
        if array_list.length >= array_list.capacity:
            new_capacity = array_list.capacity * 2
            new_list = [None] * new_capacity
            for i in range(0, index):
                new_list[i] = array_list.data[i]
            for j in range(index, array_list.length):
                new_list[j + 1] = array_list.data[j]
            new_list[index] = value
            return List(new_list, array_list.length + 1, new_capacity)
        else:
            for i in range(array_list.length - 1, index - 1, -1):
                array_list.data[i + 1] = array_list.data[i]
            array_list.data[index] = value
            return List(array_list.data, array_list.length + 1, array_list.capacity)


# list -> number
# returns number of elements in the list
def length(array_list):
    return array_list.length


# list int -> value
# returns value at index position in list
def get(array_list, index):
    if index < 0 or index >= array_list.length:
        raise IndexError()
    else:
        return array_list.data[index]


# list int value -> ArrayList
# returns resulting list after element at index position is replaced with given value
def set(array_list, index, value):
    if array_list.length <= index or index < 0:
        raise IndexError()
    array_list.data[index] = value
    return array_list


# list int -> tuple
# returns element previously at the index and resulting list
def remove(array_list, index):
    if index < 0 or array_list.length <= index:
        raise IndexError()
    else:
        value = array_list.data[index]
        array_list.length -= 1
        for i in range(index, array_list.length):
            array_list.data[i] = array_list.data[i + 1]
        return value, array_list


# list function -> None
# takes list and function and returns None
def foreach(lst, func):
    for i in range(lst.length):
        func(lst.lst[i])
    return None


# list value -> song
# takes list and returns song with attribute
def search(array_list, song_num):
    for i in array_list:
        return array_list.data[song_num]


# list function -> list
# takes list and "less-than" function and returns sorted list (ascending)
def sort(array_list, func):
    lst = array_list.data
    global length
    length = array_list.length
    for index in range(length - 1):
        small_index = index_of_smallest(lst, index, func)
        swap(lst, index, small_index)
    return array_list


# list int function -> int
# returns the index of smallest value in list
def index_of_smallest(array_list, first, func):
    index = first
    for i in range(first, length):
        if func(array_list[i], array_list[index]) is True:
            index = i
    return index


# list int int -> None
# swaps values in list
def swap(array_list, index1, index2):
    temp_index = array_list[index1]
    array_list[index1] = array_list[index2]
    array_list[index2] = temp_index
