""" 
The following code takes in a nubmer and replaces the first "6" value with a "9" to create the largest possible number.

"""


num = 9969969696

convertToList = [int(x) for x in str(num)]

def modify_list(num_list):
    i = 0
    for i in range(len(num_list)):
        if num_list[i] == 6:
            return num_list[:i] + [9] + num_list[i+1:]
    return num_list  # No change if all digits are 6
    
# Call the function and print the result
result = modify_list(convertToList.copy())

def convertToString(List):
    for i in List:
        print(i, end="")

convertToString(result)

print(result)