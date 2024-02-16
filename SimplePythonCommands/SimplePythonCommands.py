## Section 1 - variables and functions: 

# Question 1: Create two variables. One should be a string data type, and the other should be of type int.

# Use a single print statement to print both variables:

var1 = "Hello "
var2 = 42

print (var1 + str(var2))

# Question 2: Create a Python function that prints a greeting with a name as the parameter.

# Invoke the function with a name argument of your choosing:

name = "Justin"

def greeting(name):
  print ("Hello " + name)

greeting(name)

## Section 2 - lists:

# Question 3: Create a list of your favorite movies with  at least 4 elements:

movies = ["The Matrix", "The Dark Knight", "The Shawshank Redemption", "The Godfather"]

# Question 4: Use a print statement to print the list item at the index of 1:

print (movies[1])

# Question 5: Append a movie to the end of your list:
movies.append("The Godfather Part II")

# Use a print statement to print this ammended list:
print (movies)


## Section 3 - dictionaries:

# Question 6: Create a dictionary named 'cellphone' with 2 key:value pairs that are the properties of your cellphone.
#The keys should be: "color" and "number".
#Fill out the values on your own:
cellphone = {
  "color": "black",
  "number": "555-555-5555"
}

# Question 7: Access a value from inside the dictionary (Try to print the value of the 'color' property).
print (cellphone["color"])

# Question 8: Create a variable that is the dictionary's length:

length = len(cellphone)

# Question 9: Use del to remove a key:value pair that isn't one of your original 4:

del cellphone["number"]

# Question 10: Recreate the 'cellphone' dictionary:

cellphone = {
  "color": "black",
  "number": "555-555-5555"
}

# Question 11: Use a for loop to print the key:value pairs of the ammended dictionary:

for key, value in cellphone.items():
  print (key, value)

# Question 7: Access a value from inside the dictionary (Try to print the value of the 'color' property).

print (cellphone["color"])


## Section 4 - strings:

# Question 8: Create a variable and store a string with multiple words in it:
string = "Hello, my name is Justin."
# Question 9: Utilize the method that capitalizes the first letter of each word in your string - store this new string in a new variable:
new_string = string.title()
# Use a print statement to print the new string:
print (new_string)



# Bonus

# Question 10: Uncomment and look into this nested dictionary - try to relate your knowledge of objects and arrays in JavaScript.

students_in_order = {
  1: {'name': 'Esteban', 'age': '27', 'eye color': 'blue'},
  2: {'name': 'Jackson', 'age': '22', 'eye color': 'brown'},
  3: {'name': 'Zayn', 'age': '26', 'eye color': 'green'}
}
  
# Question 10 A: Write a print function that outputs the second student in the dictionary
# Add a new student to the dictionary, out of order. Do not modify the student_in_order object
print(students_in_order[2])

# Question 10 B: Write a print statement that outputs the name "Zayn" using the dictionary
print(students_in_order[3]["name"])

# Question 10 C: Write a print statment that outputs the age of Esteban from the dictionary
print(students_in_order[1]["age"])