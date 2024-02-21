# my_lst = []
alpha = "abcdefghijklmnopqrstuvwxyz"
my_lst = [x for x in alpha[0:10] ]
my_lst3 = [x for x in alpha[4:17] ]

# newlist = [x for x in fruits if "a" in x]

print(my_lst)
print(my_lst3)
# solution: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# or
beta = "abcdefghijklmnopqrstuvwxyz"
my_lst2 = [beta[i] for i in range(10)]
print(my_lst2)



# Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
#       Unsorted list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# Solution
grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_grades = sorted(grades, key = lambda x: x[1])
print(sorted_grades)


# Write a lambda function to cube every element of a list.
#       Original list: [3,6,9,2] List after lambda function: [27,216,729,8]

# Solution
cubed = lambda x: [i**3 for i in x]
print(cubed([3,6,9,2]))

# Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.
#        Input list: [3,6,9,2] List after lambda function and list comprehension: [False, True, False, True]

# Solution
even_odd = lambda x: True if x%2 == 0 else False
print([even_odd(x) for x in [3,6,9,2]])


# Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).

# Solution
nums = [i for i in range(1,101)]
print(nums)


# Use a dictionary comprehension to count the length of each word in a sentence.
#       Input: "The quick brown fox jumped over the fence." otuput: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}

# Solution
sent = "The quick brown fox jumped over the fence."
print({word:len(word) for word in sent.split()})

