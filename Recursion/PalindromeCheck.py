# Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.
#A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.

def is_palindrome(str):
  if len(str) == 1 or len(str) == 0:
    return True
  else:
    return (str[0] == str[-1]) and is_palindrome(str[1:-1])

print("is 'apple' a palindrome?")
print(is_palindrome('apple'))
print("is 'tacocat' a palindrome?")
print(is_palindrome('tacocat'))