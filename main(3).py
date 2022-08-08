import os 

# creating main function
def main():

  # creating and getting user input for directory and file name
  directory = input("Please enter the name of the Directory you want to use : ")
  file = input("Please enter the Files name : ")

  # checking for the directory and creating it if it does not exist
  if not os.path.isdir(directory):
    os.makedirs(directory)

  # Getting users name address and phone number
  name = input("Please enter your name : ")
  address = input("Please enter your address : ")
  phone = input("Please enter your phone number : ")

  # creating the file and opening it
  writeFile =  open(os.path.join(directory,file),'w')

  # writing the name,address,phone to file seperated by commas 
  writeFile.write(name+','+address+','+phone+'\n')

  #closing the file
  writeFile.close() 
  # printing the header for the file contents
  print("File Contents : ")

  #preparing to read by opening the file
  readFile = open(os.path.join(directory,file),'r') 
  # using a for loop to print the contents
  for line in readFile:
    print(line)
  #closing the file
  readFile.close()

#calling the main function to run!
main()
