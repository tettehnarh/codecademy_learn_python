# Create a function called append_size that has one parameter named my_list.

# The function should append the size of my_list (inclusive) to the end of my_list. The function should then return this new list.

# For example, if my_list was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of my_list was originally 3.

#Write your function here
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# Write a function named append_sum that has one parameter — a list named named my_list.
# The function should add the last two elements of my_list together and append the result to my_list. It should do this process three times and then return my_list.
# For example, if my_list started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
#Write your function here
def append_sum(my_list):
  counter = 0
  while counter < 3:
    sum_last_two = my_list[-1] + my_list[-2]
    my_list.append(sum_last_two)
    counter += 1

  return my_list

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# Write a function named larger_list that has two parameters named my_list1 and my_list2.
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of my_list1.
#Write your function here
def larger_list(my_list1, my_list2):
  largest_list = max(my_list1,my_list2)

  if len(my_list1) == len(my_list2):
    return my_list1[-1]
  elif len(my_list1) < len(my_list2):
    return my_list2[-1]
  else:
    return my_list1[-1]
  
#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# Create a function named more_than_n that has three parameters named my_list, item, and n.
# The function should return True if item appears in the list more than n times. The function should return False otherwise.
#Write your function here
def more_than_n(my_list, item, n):
  counter = 0
  
  for num in my_list:
    if num == item:
      counter += 1
  
  if counter > n:
    return True
  return False

# Write a function named combine_sort that has two parameters named my_list1 and my_list2.
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.
#Write your function here
def combine_sort(my_list1, my_list2):
  new_list = my_list1 + my_list2
  return sorted(new_list)

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))



#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))