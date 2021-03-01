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
print(merge_sort(list1))

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
