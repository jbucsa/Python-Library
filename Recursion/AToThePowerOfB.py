# Write a function that calculates the value of 'a' to the power of 'b'.
#For example if a=2 and b=4, then power(2,4) would be calculating 2^4=2*2*2*2 so the result would be 16.

def a_to_b(a,b):
  if b < 1:
    print("invalid input")
  elif b == 1:
    return a
  else:
    return a * a_to_b(a,b-1)

print("2^4:")
print(a_to_b(2,4))