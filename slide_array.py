array = [50, 49, 48, 47, 46, 45]

i = 0
curr = 0


def slide(currentPosition, toInsertPosition, array):
    array = array.copy()
    print("\noriginal array: {}".format(array))
    print("current position {}: {}".format(currentPosition, array[currentPosition]))
    print("to insert position {}: {}".format(toInsertPosition, array[toInsertPosition]))
    if (currentPosition > toInsertPosition):
        toInsert = array[currentPosition]
        while currentPosition - 1 >= toInsertPosition:
            array[currentPosition] = array[currentPosition-1]
            currentPosition -= 1
            print(array)
        array[toInsertPosition] = toInsert
        print(array)
    elif (currentPosition < toInsertPosition):
        toInsert = array[currentPosition]
        while currentPosition + 1 <= toInsertPosition:
            array[currentPosition] = array[currentPosition+1]
            currentPosition += 1
            print(array)
        array[toInsertPosition] = toInsert
        print(array)
    return array


slide(4, 2, array)
slide(2, 4, array)
slide(2, 2, array)

