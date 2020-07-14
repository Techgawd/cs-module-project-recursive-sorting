# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # Your code here

    # initialize indeces for both arrays
    index_a = index_b = 0
    # loop through the arrays
    while index_a < len(arrA) and index_b < len(arrB):
        # compare elements at given index
        # set smaller value at given index of merged_arr
        if arrA[index_a] < arrB[index_b]:
            merged_arr.append(arrA[index_a])
            index_a += 1
        else:
            merged_arr.append(arrB[index_b])
            index_b += 1
    merged_arr.extend(arrB[index_b:])        
    merged_arr.extend(arrA[index_a:])
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:

        return arr
    mid = int(len(arr)/2)
    # split array and call merge_sort on each half
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

