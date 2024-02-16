# Write a function that prints the natural numbers from 1 to n

def natural_numbers(x,i=1):
    #base case
  if i > x:
    return
  #recursive case
  else:
    print(i)
    natural_numbers(x,i+1)
natural_numbers(3)
#output: 1 2 3

numbers = list(range(1, 1000))

print(numbers)


