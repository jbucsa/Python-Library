# Write a program that takes a positive number as an argument and prints the numbers from n to zero

def count_down(n):

  #  Base case
  if n==0:
      return

  #  Recursive case
  else:
      print(n)
      count_down(n-1)

# test case
n=8
count_down(n)

# another solution is:
def count_down(n):
  #inherent base case
  #(will stop if n <= 0)
  if n>0:
      #recursive case
      print(n)
      count_down(n-1)
   
#test case
n=8
count_down(n)
