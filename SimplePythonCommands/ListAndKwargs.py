def manyParams(**kwargs):
 """
 This function accepts any number of named parameters and returns three lists:
 - A list of all the string parameters.
 - A list of any numerical parameters (each incremented by three).
 - A list of any non-string and non-numerical parameters.
 """

 strings = []
 numbers = []
 others = []

 for key, value in kwargs.items():
    print(key, value)
    if isinstance(value, str):
        strings.append(value)
    elif isinstance(value, bool):
        others.append(value)
    elif isinstance(value, (int, float)):
        numbers.append(value + 3)

 return strings, numbers, others


# Example usage
result = manyParams(name="Alice", age=30, city="New York", active=True)
print("Strings:", result[0])
print("Numbers:", result[1])
print("Others:", result[2])
print(result)
print(manyParams())