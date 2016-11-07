array = [50, 49, 48, 47, 46, 45]
i = 0
count = 0
while i < len(array):
    # if has next
    if(i+1 < len(array)):
        # compare to next
        if(array[i] < array[i+1]):
            i += 1
            count += 1
            continue
        else:
            # swap
            tmp = array[i+1]
            array[i+1] = array[i]
            array[i] = tmp
            count += 1
    # scan array behind
    subarray = array[0:i]
    if(len(subarray) > 1):
        j = len(subarray) - 1
        pos = i
        while j >= 0:
            if (array[pos] > array[j]):
                j -= 1
                count += 1
                continue
            else:
                tmp = array[j]
                array[j] = array[pos]
                array[pos] = tmp
                pos -= 1
                count += 1
            j -= 1

    i += 1
    print(array)