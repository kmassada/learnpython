import time
start_time = time.time()
array = [50, 49, 44, 47, 46, 45]

bubbleSorted = True
i = 0

while i < len(array):
    # if within boundary and bigger than next, swap
    if i+1 < len(array) and array[i+1] < array[i]:
        tmp = array[i]
        array[i] = array[i+1]
        array[i+1] = tmp
        bubbleSorted = False
    i += 1
    # if at end of pass and
    if(i == len(array) and not bubbleSorted):
        i = 0
        bubbleSorted = True
        print(array)

print("--- %s seconds ---" % (time.time() - start_time))

# --- 0.00191211700439 seconds ---
