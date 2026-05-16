import random

def array_gen(size):
    return[random.randint(0,100) for _ in range(size)]
    #returns -> for x in the range of size given (0, n-1) with int randomly between 0,100

#Bubble sort, compares index value (i) with next index value (i+1), swaps values of indices if (i+1) index is smaller
#to flip order value swap the comparrison and swap values if (i+1) index value is larger than (i) index value
def bubble_sort(arr):
    arr = arr.copy()
    for num_pass in range(len(arr)): #indices from range 0-9 = 10 passes, pass for each value
        for i in range(len(arr)-1): #loops through range but stops at -1 of the arr len so i+1 is not out of bounds
            if arr[i]>arr[i+1]: #if x index value is greater than next index value
                arr[i],arr[i+1] = arr[i+1], arr[i] #swap the values of the indices
    return arr #return the array 

#Selection sort, compares all values of an array and moves smallest value to first index, loops through list with smaller 
#and smaller values in the given range
def selection_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        min_val=min(arr[i:])
        min_idx = arr[i:].index(min_val) + i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#Insertion sort, moves larger elements to the right to make space, and the current value ends up moving left into its correct position.
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)): #starts range from 1 - len of array ex. arr[10] range is now equal to 1 to 9 instead of 0-9
        val = arr[i] #sets value equal to value of index 1 instead of zero as usual
        j = i - 1 #j is now bieng shifted to be the index always to the left of i, in this case 0
        while j >=0 and arr[j]>val: #while j is greater than or is the index 0 and the value of index j is greater than the value of index i
            arr[j+1]=arr[j] #make the value of index j move to the right
            j-=1 #decreases j index by 1
        arr[j+1] = val #assigns value of arr[i] to the index left of arr[j]
    return arr

#Split array until its only 1 element per sub array, then reassembly in order "merge"
#We split until each element is alone (already sorted), then merge them in order.
def merge_sort(arr):
    merged = []
    i=0
    j=0

    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    right = merge_sort(right)
    left = merge_sort(left)

    while i < len(left) and j <len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
  
def quick_sort(arr): #organizes around a pivot, fastest and most efficent algo 

    if len(arr)<=1: #recursive stopping algo
        return arr
    pivot_val = random.choice(arr) #chooses a random pivot val
    left = [x for x in arr if x<pivot_val]
    pivot = [x for x in arr if x==pivot_val]
    right = [x for x in arr if x>pivot_val]

    arr = left + pivot + right
    return quick_sort(left) + pivot + quick_sort(right)

import time
arr = array_gen(10000)

start = time.time()
bubble_sorted = bubble_sort(arr)
bubble_time = end = time.time() - start

start = time.time()
selection_sorted = selection_sort(arr)
selection_time = end = time.time() - start

start = time.time()
insertion_sorted = insertion_sort(arr)
insertion_time = end = time.time() - start

start = time.time()
merge_sorted = merge_sort(arr)
merge_time = end = time.time() - start

start = time.time()
quick_sorted = quick_sort(arr)
quick_time = end = time.time() - start

times = {
    "Bubble": bubble_time,
    "Selection": selection_time,
    "Insertion": insertion_time,
    "Merge": merge_time,
    "Quick": quick_time
}

fastest = min(times, key=times.get)

for sort_name, sort_time in times.items():
    if sort_name == fastest:
        print(f"{sort_name} sort time: {sort_time:.6f} seconds <-- FASTEST")
    else:
        print(f"{sort_name} sort time: {sort_time:.6f} seconds")