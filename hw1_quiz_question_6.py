# Quiz Question

For this question, create and submit a .py file that does the following:


1. Initialize a list, A, with values of your choice.

2. Using a for-loop, set the list, B, to the reversed version of A (do not use .reverse).

3. If A is identical to its reverse, print "A is a palindrome"; otherwise, print "A is not a palindrome".

(eg. if A = "app", then B = "ppa" and A will not be a palindrome.) if A is ['a', 'p', 'p'] then B is ['p', 'p', 'a'] and A is not a palindrome.)
"""

# a = [1,"hello",2,"Shivam"]
a = ['p', 'a', 'p']
b = []

for i in range(len(a)-1,-1,-1):
    b.append(a[i])

if a == b:
    print("A is a palindrome")
else:
    print("A is not a palindrome")

