array = [50, 49, 44, 47, 46, 45, 26, 32]

# divide array into 2
array1 = array[0:len(array)/2]
array2 = array[len(array)/2:]


def splitArray(array):
    print(array)
    if len(array) == 1:
        return [array[-1]]
    else:
        return [splitArray(array[0:len(array)/2]), splitArray(array[len(array)/2:])]


def sortMerge(array1, array2):
    # while has element
    while len(array1)  and len(array2) == 2


results = splitArray(array)
print(results)
