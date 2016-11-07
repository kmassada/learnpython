array = [50, 49, 44, 47, 46, 45]

swapped = False
j = 0
while j < len(array):
    print(array)
    # find min
    i = j
    minimum = array[i]
    position = i
    while i < len(array):
        if array[i] < minimum:
            minimum = array[i]
            position = i
        i += 1
    # swap
    if not position == j:
        tmp = array[j]
        array[j] = array[position]
        array[position] = tmp
        swapped = True
    j += 1
