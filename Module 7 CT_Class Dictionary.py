#need directory for where .txt files are, should be put in current directory where .py script is
from pathlib import Path


#function for opening passed in .txt then creat a dictionary and return dictionary
def open_file_with_pathlib_return_dictionary(file_name):
   script_dir = Path(__file__).resolve().parent
   file_path = script_dir / file_name

   with open(file_path, 'r') as file:
      content = file.readlines()

   dictionary = {}

   for line in content:
      key, value = line.strip().split(';')
      dictionary[key.strip()] = value.strip()

   #return newly created dictionary
   return dictionary


#Main Code empty dictionaries
rooms = {}
time = {}
instructors = {}

#open rooms.txt and read file create dictionary in function
rooms = open_file_with_pathlib_return_dictionary('rooms.txt')

#create dictionary with function
instructors = open_file_with_pathlib_return_dictionary('instructors.txt')

#create dictionary with function
time = open_file_with_pathlib_return_dictionary('time.txt')

control = True
#while loop for recursive output of class, time and instructor
while control is True:
    

    #Print the list of courses
    print("\nThe courses are:")
    for cls in rooms:
        print(cls)

    #input for selection of class or e exit 
    selection = input('\nWhat course are you looking for? Enter e to exit ')
    print('\n')

    #exit while loop if e is entered
    if selection == 'e':
        print('Exiting, By')
        control = False
    
    #elif for if selection key is in room dictionary
    elif selection in rooms:
        
        print('Class', selection, 'meets in room: ', rooms[selection])
        print('at time:', time[selection])
        print('and is taught by Professor', instructors[selection])
      
        control = True
    
    #invalid entry   
    else:
        print('Incorrect selection, please try again.')
        control = True   

      