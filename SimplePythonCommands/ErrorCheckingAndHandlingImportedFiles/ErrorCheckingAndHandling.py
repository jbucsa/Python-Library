class FileManipulator:
  def __init__(self, fileName):
    self.contents = None
    while self.contents == None:
      try:
        myfile = open(fileName, 'r') # Open a file for 
        self.contents = myfile.readlines() # Read in the content by line.
      except (FileNotFoundError, TypeError, OSError) as e:
        print(type(e), e)
        fileName = input("Please enter a valid file name: ")
      else:
        myfile.close()
      
  def reverse(self,fileName):
    while True:
      try:
        myfile = open(fileName, 'w') # Open a file for writing
        revContent = [x.strip()[::-1] for x in self.contents]
        for i in range(len(revContent)):
          if i == (len(revContent)-1):
            myfile.write(revContent[i])
          else:
            myfile.write(revContent[i] + '\n') # write desired output to file
      except (FileNotFoundError, TypeError, OSError) as e:
        print(type(e),e)
        fileName = input("Please enter a valid file name: ")
      else:
        myfile.close()
        break
  
  #bonus
  def upper(self,fileName):
    while True:
      try:
        myfile = open(fileName, 'w') # Open a file for writing
        upperContent = [x.strip().upper() for x in self.contents]
        for i in range(len(upperContent)):
          if i == (len(upperContent)-1):
            myfile.write(upperContent[i])
          else:
            myfile.write(upperContent[i] + '\n') # write desired output to file
      except (FileNotFoundError, TypeError, OSError) as e:
        print(type(e),e)
        fileName = input("Please enter a valid file name: ")
      else:
        myfile.close()
        break
        

f = FileManipulator(input("Please enter the name of the file you would like to read: "))
print(f.contents)


f.reverse("tmp2.txt")
f.upper("tmp3.txt")

# Print file "tmp2.txt"
fileName2 = "tmp2.txt"
myfile2 = open(fileName2, 'r') # Open a file for reading.
contents2 = myfile2.readlines() # Read in the content by line.
myfile2.close() # Explicitly close the file
print(contents2) #print the contents of the file