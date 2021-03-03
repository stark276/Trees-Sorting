#!python

def is_sorted(items):

 #TODO: write code to implement the selection sort algorithm
 for i in range(len(items)):
  #moving the boundary of the sorted section forward

  min_location = i

  for j in range(i + 1, len(items)):
   #finding the min value location in the unsorted section
   if items[j] < items[min_location]:

    min_location = j

  temp = items[i]
  items[i] = items[min_location]
  items[min_location] = temp

items = [3,1,7,0]
        #i i j-> 
is_sorted(items)
#print(items) #should print [0, 1, 3, 7]
 






def bubble_sort(list_a):
    '''
    Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    '''
    indexing_length = len(list_a) - 1 #SCan not apply comparision starting with last item of list (No item to right)
    sorted = False #Create variable of sorted and set it equal to false

    while not sorted:  #Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length): # For every value in the list
            if list_a[i] > list_a[i+1]: #if value in list is greater than value directly to the right of it,
                sorted = False # These values are unsorted
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #Switch these values
    return list_a # Return our list "unsorted_list" which is not sorted.


# print(bubble_sort([4,8,1,14,8,2,9,5,7,6,6]))

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) because as the numbers of items grow the so does the outter and inner loop, also the function increases in a quadratic way
    Memory usage: O(1) because as items grow no additional spaces are created and everything done in place"""

    # pseudo seperates list into 2 sections, sorted and unsorted, goes through the unsorted section and finds the index with lowest value among all and swaps it with the sorted section

    ## can use while or for outter loop
    # i = 0
    # this is 'sorted' section
    # while i < len(items) - 1:
    for i in range(len(items)-1):
        lowest_index = i
        lowest_value = items[lowest_index]
        # this is 'unsorted' section
        for j in range(lowest_index + 1, len(items)):
            if items[j] < lowest_value:
                # lowest_index gets updated and settles with the lowest index of lowest value
                lowest_index = j
                lowest_value = items[j]
        # performs the swap
        items[i], items[lowest_index] = items[lowest_index], items[i]
        # moves pointer up
        # i += 1

    return items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2) because as items grow outter and inner loop both increases, also the function increases in a quadratic way
    Memory usage: O(1) because everything is done in place """

    # similar to selection sort where list is pseudo broken into 'sorted' and 'unsorted' sections
    # an item is selected from 'unsorted' and checks against the 'sorted' section to see where to add

    # this is our selection section of the list
    for i in range(1, len(items)):
        # range is non inclusive so i is never reached only i-1
        # loop through our 'sorted' section
        for j in range(0, i):
            # the moment it finds an item in this part of the list which is greater or equal 'unsorted' selected item, it is removed from the 'unsorted' section and inserted into the 'sorted' section
            if items[j] >= items[i]:
                removed_item = items.pop(i)
                items.insert(j, removed_item)
                continue
    return items
