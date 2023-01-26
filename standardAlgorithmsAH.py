# ---------- Bubble Sort ---------- # 

def bubbleSort(array):
    # Initialises swapped to keep track of if something has been swapped in an itteration
    # Initialises length
    swapped = True
    length = len(array)-1
    # While something has been swapped (Not sorted)
    while swapped:

        # On a new iteration, nothing could have been swapped
        swapped = False
        
        # Creates a loop to iterate through the lists effective length
        for i in range(length):
            # If a number is larger than the number after (Not in order)...
            if array[i] > array[i+1]:
                # Then swap the numbers position
                temporary =  array[i]
                array[i] = array[i+1]
                array[i+1] = temporary
                # Set swapped to true
                swapped = True
        # After iterating through the whole list, reduce length by 1
        length -= 1
        # Keep looping until the whole list has been sorted
    return array


# ---------- Insertion Sort ---------- #

def insertionSort(array):

    # Starts a loop which will repeat over the length of the array (from the 1st index)
    for i in range(1, len(array)):
            
        # In this iteration, keep the Ith value aside
        value = array[i]
        # Also keep a copy of the index which is mutable
        index = i

        # While the value we have is smaller than the index before AND while the index is greater than 0
        while value < array[index-1] and index > 0:
            # Move the value in index-1 up to index
            array[index] = array[index-1]
            # Reduce index by 1
            index -= 1

        # Once you have exited the while loop (array[index-1] is smaller than value, therefor value is in the right place,
        # or if we're at the start of the list), value is in the right place, so set array[index] as value
        array[index] = value

    # Once you've done this for every element in the list, you now have a sorted list
    return array


# ---------- Binary Search ---------- #

def binarySearch(target, array):

    print(target)
    
    s = 0
    e = len(array)
    found = False
    
    while not found and e > s:

        print(array) 
        
        m = int((e+s)/2)
        
        if target > array[m]:
            s = m+1
            
        elif target < array[m]:   
            e = m-1
            
        else:
            found = True

    if found:
        return m
    else:
        return None

