# Worksheet 3

Link : https://bcourses.berkeley.edu/courses/1557109/files/95167724?module_item_id=17806750

# Ques 1. Write a function called ’calculate mean’ that calculates the mean of numbers in a list.
"""

def calculate_mean(list1):

  sum_of_number = 0

  for i in list1:
    sum_of_number+=i

  number_of_ele = len(list1)

  avg = sum_of_number/number_of_ele
  return avg

input_list = [1,2,3,4]
print(calculate_mean(input_list))

"""# Ques 2 Modify your calculate mean function in two ways1: it asserts that a list is passed in, raising an error otherwise, and 2: if some item of the list is not an int or float, that list item is simply skipped (so you could run calculate mean([2,6,’hi’,7.3]), for example)"""

def calculate_mean(list1):

  assert type(list1) is list, "Input should be a list"

  sum_of_number = 0
  number_of_ele = 0

  for i in list1:

    if (type(i)!=int and type(i)!=float):
      continue

    else:
      sum_of_number += i
      number_of_ele += 1

  if number_of_ele == 0:
    raise ValueError("Only int/float is allowed or list is empty.")

  avg = sum_of_number/number_of_ele
  return avg

input_list = [1,2,3,4,"hi"]
print(calculate_mean(input_list))

"""# Ques 3 : Write a function called myMaxMin that returns both the maximum and the minimum entry of a list of numbers. Then, modify it to allow us to optionally add a (boolean) input make positive that is False by default, but makes the function return 0 in place of the max or min if they are negative when make positive is specified to be True. Test that you can call the function with or without adding the make positive input"""

def myMaxmin(list1, max_boolean_input = False, min_boolean_input = False):

  max_value, min_value = list1[0], list1[0]

  for i in range(1,len(list1)):
    if list1[i] >= max_value:
      max_value = list1[i]
    elif list1[i] < min_value:
      min_value = list1[i]

  if max_boolean_input == False:
        max_value = 0
  if min_boolean_input == False:
        min_value = 0

  return max_value, min_value


list1 = [12,1,2,3,4,5,6]

max_value, min_value = myMaxmin(list1, True, True)
print(f'max: {max_value}, min: {min_value}')

max_value, min_value = myMaxmin(list1)
print(f'max: {max_value}, min: {min_value}')

"""# Question 4 Define a function that takes integers as inputs and returns f (N ) = NX i=1 sin(i) · i Next, write a for loop to find the integer between 0 and 100 that maximizes f"""

import math

def sin_running_sum(n):

  assert type(n) is int, "input should be integer"

  if n == 0:
    return 0

  return (math.sin(n)*n) + sin_running_sum(n-1)


print(sin_running_sum(10))

max_value = 0
max_int = 0

for i in range(101):

  value = sin_running_sum(i)

  if value > max_value:
    max_value = value
    max_int = i

print(f'The func will maximise on ele:{max_int}, with value {max_value}')

"""# Ques 5 optional if you have time, does not need to be turned in) Write a function calculate volatility(points) that measures a player’s scoring consistency. It should call your calculate mean function from Question 1 to find the player’s average deviation from their average score: calculate the player’s average score across games, then calculate and return the mean of the absolute differences between each individual game score and that average. Next, write a function scout player(name, points) that computes a player’s average and volatility, then prints a short remark: If their volatility is less than 5, print ”Highly Consistent”; otherwise, print ”Flagged for consistency issues”. Test yourfunctions on alice = [15, 17, 16, 15, 17, 16] and bob = [30, 2, 28, 4, 32,0]. Both average 16 points, but have very different playstyles!"""

def volatility(points):

  avg = calculate_mean(points)
  avg_deviation = 0

  for i in points:
    avg_deviation += abs(i-avg)

  avg_deviation = avg_deviation/len(points)

  return avg_deviation

def scout_player(name, points):

  avg = calculate_mean(points)
  vol = volatility(points)

  if vol < 5:
    print(f'{name} is Highly Consistent')
  else:
    print(f'{name} is Flagged for consistency issues')


alice = [15, 17, 16, 15, 17, 16]
bob = [30, 2, 28, 4, 32,0]

vol_a = volatility(alice)
vol_b = volatility(bob)

print(f'average of alice: {calculate_mean(alice)}')
print(f'average of bob: {calculate_mean(bob)}')

print(f'volatility of alice: {vol_a}')
print(f'volatility of bob: {vol_b}')

scout_player('alice', alice)
scout_player('bob', bob)

