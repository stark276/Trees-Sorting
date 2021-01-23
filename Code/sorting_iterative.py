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
print(items) #should print [0, 1, 3, 7]
 


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order


def selection_sort(items):
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
