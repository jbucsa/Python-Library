list_of_values = ['a', 'b', 'c', 'd', 'e']


def function1(values):
  for value in values:
    # for X in VALUES
    # The output scales based on the number of elements in the list. This means the function has linear complexity, O(n).
    print(value)

def function2(values):
    # The values at index 0 and 1 stay the same regardless of whether the list size grows. Technically, adding each section would give us O(1) + O(1) = O(2), but O(2) is a constant, so we would be left with O(1). In other words, adding two constants results in a constant.
    # X = 0
  print(values[0])
    #  X = 1 
  print(values[1])

def function3(values):
    # Each value in the list has n outputs, so we have n*n = n^2 for the number of outputs. This means the function has quadratic complexity, O(n^2).
  for x in values:
    for y in values:
      print(x, y)

def function4(values):
  for i in range(4):
    print("Python is great")
  
  print("Software Engineering is awesome!")
  print("Software Engineering is awesome!")
  
  for value in values:
    print(value)

  for value in values:
    print(value)
    # The time complexity is linear, O(n). When we break down each section, we have: O(4) + O(2) + O(n) + O(n) = 6 + O(2n). As n gets larger and larger (closer and closer to infinity), the dominant term we are left with is n. This is why the time complexity is linear, O(n).

# It may be helpful to comment out all of the functions beside the function you are focusing on. This can help with determining the output of the function you are analyzing.
    

def function5(n):
  test_list=[]

  for num in range(n):
    test_list.append('add me')

  return test_list
    #  This is still a Linear Function. 
print(function5(3))



function1(list_of_values)
function2(list_of_values)
function3(list_of_values)
function4(list_of_values)


def sum_of_list(numberedList):
  listSum = 0
  for i in numberedList:
    listSum = listSum + i
  return listSum

print(sum_of_list([1,4,3]))

# O(n) time complexity