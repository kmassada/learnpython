array = [50, 49, 48, 47, 46, 45]

holePosition = 0
valueToInsert = 0
count = 0
i = 0
while i < len(array):
    # /* select value to be inserted */
    valueToInsert = array[i]
    holePosition = i
    print(array)
    # /*locate hole position for the element to be inserted */
    while holePosition > 0 and array[holePosition-1] > valueToInsert:
        array[holePosition] = array[holePosition-1]
        print(array)
        holePosition = holePosition - 1

    # /* insert the number at hole position */
    array[holePosition] = valueToInsert
    print(array)
    print('\n')
    i += 1
