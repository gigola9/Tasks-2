def checkLists(a, b):
    state = False
    for i in a:
        if i in b:
            state = True
    return state


first = [1, 2, 3, 4, 5]
second = [5, 6, 7, 8, 9]
third = [10, 11, 12, 13]
print(checkLists(first, second))
print(checkLists(first, third))
