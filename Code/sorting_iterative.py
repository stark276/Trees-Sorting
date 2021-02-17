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


print(bubble_sort([4,8,1,14,8,2,9,5,7,6,6]))

def selection_sort(items):
  arr = []
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
