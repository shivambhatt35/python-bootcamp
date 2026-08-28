# Worksheet 4

Link : https://bcourses.berkeley.edu/courses/1557109/files/95167726?module_item_id=17806751
"""

# Initializing libraries
import numpy as np

"""# Ques 1. Initialize a 10x10 Numpy array using np.zeros or np.empty. Then, modify it so that each index i row is [i, i+1, ..., i +9]. Next, separately print each column of the resulting array."""

a = np.zeros((10,10), dtype = np.int32)

for i in range(10):
  a[i] = np.arange(i,i+10)

print(a)

"""# Question 2.  Initialize a 6x6 array of ones. Print the the right ”half” (3rd column onwards), and the bottom half (3rd row onwards). Next, set the entries of those to be zeros, without using for loops, and print the entire modified array to check it worked (so only the top-left quadrant will have ones)."""

a = np.ones( (6,6), dtype = np.int32 )

print(a[3:, :])

print(a[:, 3:])

a[3:, :] = np.zeros((3,6), dtype = np.int32)

a[:, 3:] = np.zeros((6,3), dtype = np.int32)

print(a)

"""# Question 3 Assign a variable an array taking values sin(0), sin(0.001), sin(0.002), ..., sin(3.999), sin(4). Find the largest change between two consecutive entries in that array."""

a = np.arange(0,4,.001, dtype=np.float32)

a = np.sin(a)

max_change = 0
for i in range(1,len(a)):
    change = abs(a[i]- a[i-1])

    max_change = max(max_change, change)

print(max_change)

"""# Ques 4 Solve the previous problem without using a for loop, but using only numpy arrays and numpy functions instead."""

a = np.arange(0,4,.001, dtype=np.float32)

a = np.sin(a)

result = np.abs(np.diff(a))

max_change = np.max(result)

print(max_change)

"""# Question 5 Revisit the function from worksheet 3: f (N ) = NX i=1 sin(i) · i Vectorize this function, i.e. write it with Numpy without using for-loops. How much faster is the vectorized version for large values of N? Compute and compare the runtimes for large values of N"""

import math, time

start_time = time.time()

def sin_running_sum(n):

  assert type(n) is int, "input should be integer"

  if n == 0:
    return 0

  return (math.sin(n)*n) + sin_running_sum(n-1)

n = int(input("Enter n: "))

b = sin_running_sum(n)

end_time = time.time()

recurrsion_time = end_time - start_time

print(f'Time taken for recurssion : {recurrsion_time}')

# Numpy

start_time = time.time()

n = int(input("Enter n: "))

a = np.arange(0,n,1, dtype=np.float32)
a = np.sin(a)
a = np.multiply(a[0], np.arange(0,10,1, dtype=np.float32))
b = np.sum(a)


end_time = time.time()

numpy_time = end_time - start_time

print(f'Time taken for numpy : {numpy_time}')

print(f'The ratio of numpy_time to recurssive time is : {numpy_time/recurrsion_time}')

"""# Question 6 optional if you have time, does not need to be turned in) Write a function has repeat(A)that, if given a list / numpy array list A as input, returns True if A contains a repeated number(ie some number appears twice in the array), and False otherwise. Next, rite a function generate birthdays(M) that generates a list/numpy array of M birth-days, random numbers from 1 to 365. Next, write a for loop that 10,000 times generates a such a list of 25 birthdays, and checks how often a list of birthdays has a shared birthday (one birthday appearing at least twice in the list - can you use your has repeat function?). This gives an estimate via simulation of the probability that in a room of 25 people, there are two with the same birthday!"""

def has_repeat(A):
    A = np.asarray(A)
    return len(np.unique(A)) < len(A)

def generate_birthdays(M):
    return np.random.randint(1, 366, size=M)  # 1 to 365 inclusive

n = 10000
count_shared = 0

for _ in range(n):
    birthdays = generate_birthdays(25)
    if has_repeat(birthdays):
        count_shared += 1

prob_estimate = count_shared / n_trials
print(f"Estimated probability: {prob_estimate:.4f}")

