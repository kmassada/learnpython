array = [50, 49, 48, 47, 46, 45]

i = 0

# process array
while i < len(array):
    # get number to be inserted
    position = i
    swap = array[i]

    # get position to insert
    # while left value is bigger than next
    while position > 0 and array[position-1] > swap:
        # slide array down
        array[position] = array[position-1]
        position = position - 1

    array[position] = swap
    print(array)
    i += 1
