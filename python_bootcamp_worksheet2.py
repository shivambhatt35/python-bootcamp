# Worksheet 2

Worksheet Link :
https://bcourses.berkeley.edu/courses/1557109/files/95155323?module_item_id=17804485

# Question 1

1. There is a pair of integers x, y such that x2 + y2 = 223065. Use for or while loops to
find them
"""

import math

# Declaring variables
x, y = 0, 0
n = 223065

# Looping x through 0 to root(n) and y through root(n) to i+1
for x in range(int(round(math.sqrt(n),0)+1)):
  for y in range(x+1):
    if x**2 + y**2 == n: # Checking if the logic is satisfied
      print(x, y)
      break # Break out of loop when codition is met

"""# Question 2

2. Define W0 = 2 and Wn = W Wn−1
n−1 for all integers n ≥ 1. Use a while loop to find the
smallest n such that Wn > 10
"""

# Declaring Variables
n = 0
wo = 2
wn = wo
threshhold = 10**30

# Looping till condition is satified
while wn <= threshhold:
  n+=1
  wn = wn**wn # Updating the value recursively

print(f'The values are n: {n} and wn:{wn}')

"""# Question 3

 Create a list of length 10 where entry i has value 02 + 12 + 22 + ... + i2 (without using
the formula for that if you happen to know it). Can you do it with only one for loop?
"""

# Initializing the list and variables
list1 = []
listlength = 10
running_sum = 0

# Updating the running sum
for i in range(listlength):
    running_sum += i**2
    list1.append(running_sum)

print(list1)

"""# Question 4

Set n = 100 and create two nested for loops iterating i and j through range(n). Can you
find a way to exit both for loops when i = 49 and j = 76? So after you run it, i should
have value 49 and j should have value 76

"""

# Initializing the variable
n = 100

# Looping through the 0,n
for i in range(n):
  for j in range(n):

    if (j == 76) and (i==49): # Checking the condition
      break # Breaking out of second Loop

  if i == 49:
    break # Breaking out of first loop

print(i,j)

"""# Question 5

Set A to be a list of numbers of your choice. Set B equal to A. Use for loops to set
each entry in B equal to itself plus all the ’later entries’ (entries corresponding to a larger
index) in B. After doing that (to B only), what is the value of A?
"""

# Intitializing the variables
a = [i for i in range(10)]
b = a

# Calculating the mid point
mid = int(len(b)/2)

# Updating values for "higher indexes"
for i in range(mid,len(b)):
  b[i]+=1


print(a)
print(b)

