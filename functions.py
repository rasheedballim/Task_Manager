import os

FILEPATH = "list.txt"
def read_list(filepath=FILEPATH):
    """
    reads text line by line from a txt file and stores it in list_local
    :param filepath: the file path of the txt file data is being read from
    :return: returns the list which contains each line with an index
    """
    if os.path.exists('list.txt') == False:
        open('list.txt', 'w')
        pass
    file_local = open(filepath, 'r')
    list_local = file_local.readlines()  ## YOU DONT NEED TO ADD 'LIST = []' BEFORE WHILE LOOP BECAUSE ".READLINES CREATES A LIST ALREADY AND WE CALLING THAT LIST 'LIST' "
    file_local.close()
    return list_local

def write_to_file(list_name,filepath=FILEPATH):
    """
    writes text from a list to a file, each index goes on a seperate line
    :param list_name: name of the list will be added here as an argument
    :param filepath: the file path of the txt file data is being written to
    :return: returns nothing because it just writes to a file and thats it
    """
    file = open(filepath, 'w')
    file.writelines(list_name)
    file.close()

if __name__=="__main__":
    print("this is the functions.py file")