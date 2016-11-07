import time
start_time = time.time()
array = [50, 49, 44, 47, 46, 45]

# on the assumption the maximum could only be x**2
# we loop over the len twice

for el in array:
    swapped = False
    i = 0
    while i < len(array):
        # if within boundary and bigger than next, swap
        if i+1 < len(array) and array[i+1] < array[i]:
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp
            swapped = True
        i += 1
        # if at end of pass and
    if(not swapped):
        break
    print(array)

print("--- %s seconds ---" % (time.time() - start_time))


