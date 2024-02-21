#  Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

'''
Make sure to answer the following questions about your coding process:

Q1. How does this solution ensure data immutability?
    A. 

Q2. Is this solution a pure function? Why or why not?
    A.

Q3. Is this solution a higher order function? Why or why not?
    A.

Q4. Would it have been easier to solve this problem using a different programming style?
    A.
Q5. Why in particular is functional programming a helpful paradigm when solving this problem?
    A.

'''