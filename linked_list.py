# a AnyList is one of
# - None, or
# - Pair(first, rest)


class Pair:
    def __init__(self, first, rest):
        self.first = first  # a value
        self.rest = rest    # a AnyList

    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)

    def __repr__(self):
        return ("Pair({!r}, {!r}, {!r})"
                .format(self.first, self.rest))


# -> None
# returns an empty list
def empty_list():
    return None


# list int value -> AnyList
# returns resulting list after value is placed at index position
def add(linked_list, index, value, count=0):
    if linked_list is None:
        if index == 0:
            return Pair(value, None)
        else:
            raise IndexError()
    elif index > 0:
        return Pair(linked_list.first, add(linked_list.rest, index - 1, value))
    elif index == 0:
        return Pair(value, Pair(linked_list.first, linked_list.rest))
    else:
        raise IndexError()


# list -> number
# returns number of elements in the list
def length(linked_list):
    if linked_list is None:
        return 0
    else:
        return 1 + length(linked_list.rest)


# list int -> value
# returns value at index position in list
def get(linked_list, index):
    if linked_list is None or index < 0:
        raise IndexError()
    else:
        if index == 0:
            return linked_list.first
        else:
            return get(linked_list.rest, index - 1)


# list int value -> AnyList
# returns resulting list after element at index position is replaced with given value
def set(linked_list, index, value):
    if index < 0 or linked_list is None:
        raise IndexError()
    else:
        if index == 0:
            return Pair(value, linked_list.rest)
        elif index > 0:
            return Pair(linked_list.first, set(linked_list.rest, index - 1, value))


# remove helper function
# AnyList Int -> AnyList
def remove_helper(linked_list, index):
    global rem
    if index < 0 or linked_list is None:
        raise IndexError()
    else:
        if index > 0:
            return Pair(linked_list.first, remove_helper(linked_list.rest, index - 1))
        else:
            rem = linked_list.first
            return linked_list.rest


# list int -> tuple
# returns element previously at the index and resulting list
def remove(linked_list, index):
    global rem
    if index < 0 or linked_list is None:
        raise IndexError()
    elif index == 0 and linked_list.rest is None:
        return None
    elif index == 0:
        rem = linked_list.first
        new_pair = linked_list.rest
    else:
        new_pair = Pair(linked_list.first, remove_helper(linked_list.rest, index - 1))
    return rem, new_pair


# list function -> None
# takes list and function and returns None
def foreach(linked_list, func):
    if linked_list is not None:
        func(linked_list.first)
        return foreach(linked_list.rest, func)
    return None


# list value -> song
# takes list and returns song with attribute
def search(linked_list, song_num):
    if song_num == 0:
        return linked_list.first
    else:
        return get(linked_list.rest, song_num - 1)


# list function -> list
# takes list and "less-than" function and returns sorted list (ascending)
def sort(linked_list, func):
    return_list = Pair(linked_list.first, None)
    while linked_list.rest is not None:
        new_list = linked_list.rest
        return_list = insert(return_list, new_list.first, func)
        linked_list = linked_list.rest
    return return_list


# list value function -> List
# returns sorted list including new value
def insert(list, value, func):
    if list is None:
        return Pair(value, None)
    else:
        if func(list.first, value) is True:
            return Pair(list.first, insert(list.rest, value, func))
        else:
            return Pair(value, list)
