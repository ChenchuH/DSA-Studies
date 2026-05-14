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

arr = array_gen(10)
arr_sort = bubble_sort(arr)
selection_sort = selection_sort(arr)
print(f"Original array",arr)
print(f"Bubble sort: ",arr_sort)
print(f"selection sort: ",selection_sort)