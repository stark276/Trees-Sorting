#!python

def merge(items1, items2):
  """Merge given lists of items, each assumed to already be in sorted order,
  and return a new list containing all items in sorted order.
  Running time: ??? Why and under what conditions?
  Memory usage: ??? Why and under what conditions?"""
  #TODO: Repeat until one list is empty
  i = 0
  j = 0
  len1 = len(items1)
  len2 = len(items2)
  arr1 = items1
  arr2 = items2
  arr = []

  # TODO: Find minimum item in both lists and append it to new list
  while((i<len1) and (j<len2)):
    if arr1[i] < arr2[j]:
      arr.append(arr1[i])
      i= i + 1
    else:
      arr.append(arr2[j])
      j = j + 1

  # TODO: Append remaining items in non-empty list to new list
  while i < len1:
    arr.append(arr1[i])
    i = i + 1
  while j < len2:
    arr.append(arr2[j])
    j=j+1
  return arr

# print(merge([3,25,40,55], [10,20,30]))


def merge_sort(my_list):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if len(my_list) == 1:
      return my_list
    #recursive case
    # Split items list into approximately equal halves
    middle_index = len(my_list)//2
    left_list = my_list[:middle_index]
    right_list = my_list[middle_index:]
    #Sort each half by recursively calling merge sort
    left_result = merge_sort(left_list)
    right_result = merge_sort(right_list)
    #Merge sorted halves into one list in sorted order
    return merge(left_result, right_result)
list1 = [3,25,40,55,10,20,30]
# print(merge_sort(list1))

        

def partition(array, start, end):
  pivot = array[start]
  low = start + 1
  high = end
  #array = [3,1,4,2,5]
  #  [3,1,2,4,5]
  # [3,1,2,4,5]

  while True:
    
    
  
    # If the current value we're looking at is larger than the pivot
    # it's in the right place (right side of pivot) and we can move left,
    # to the next element.
    # We also need to make sure we haven't surpassed the low pointer, since that
    # indicates we have already moved all the elements to their correct side of the pivot
    while low <= high and array[high] >= pivot:
      high = high - 1
      # stands on 2

    # Opposite process of the one above
    while low <= high and array[low] <= pivot:
      low = low + 1
      # meet each other at 2
    
    # We either found a value for both high and low that is out of order
    # or low is higher than high, in which case we exit the loop
    if low <= high:
      array[low], array[high] = array[high], array[low]
        # The loop continues
    
    else:
        # We exit out of the loop
      break
  
  array[start], array[high] = array[high], array[start]
  print(high)

  return high
  

def quick_sort(array, start, end):
  #base case
  if start >= end:
    return
  #recursive case
  p = partition(array, start, end)
  # print(p)
  quick_sort(array, start, p-1)
  quick_sort(array, p+1, end)



array = [3,1,4,2,5]

quick_sort(array, 0, len(array) - 1)
print(array)