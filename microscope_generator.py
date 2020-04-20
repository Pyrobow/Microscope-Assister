import os
import networkx
from dice_class import Dice

#Constants

data_dir = os.path.dirname(__file__) + "/Data"

#Function

"""Gets data from a file
Retrieves the data from a file in the form of a lst. Each member of the list is a 
line in the original file.

Args:
    directory (str): The path to the file
    filename (str): The name of the file you want to get data from

Returns:
    temp_lst (lst): A list with line of the file as an entry
"""

def get_data_from_file(directory,filename):
    temp_lst = []
    file1 = open(directory +"/"+ filename,"r")
    for line in file1:
        temp_lst.append(line)
    file1.close()
    return temp_lst

"""Runs a randomiser on a list

Args: 
    lst (lst): A list containing the entries you want the generator to work on
"""

def generator_simple(lst):
    dn = Dice(len(lst)-1)
    print(lst[0].strip("\n"))
    print(lst[dn.roll()].strip("\n"))
    print("\n")

def generator_type(lst):
    dn = Dice(len(lst)-1)
    print(lst[0].strip("\n"))
    print(lst[dn.roll_weighted(35,40,25)].strip("\n"))
    print("\n")

"""Iterates through files

This function iterates through files in a folder and then runs the appropriate randomizer.

Args:
    folder (str): The folder containing the files you want iterated over.

Returns:
"""

def file_iterator(folder):
    directory_in_str = data_dir +"/"+folder
    directory = os.fsencode(directory_in_str)
    for file in os.listdir(directory):
        data = []
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            data = get_data_from_file(directory_in_str,filename)
            if filename == "type.txt":
                generator_type(data)
            else:
                generator_simple(data)

#UI

ex = 0 
while ex == 0:
    ask = input("Do you want to generate something?(Y/N) ")
    if ask.upper() == "Y":
        file_iterator("Main")
    else:
        ex = 1