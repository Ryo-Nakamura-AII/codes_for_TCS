
import os
from datetime import datetime
  
# checking if the directory demo_folder 
# exist or not.

    
def get_file_name():
    current_datetime = datetime.now()
    cdt = current_datetime.strftime("%m%d-%H%M")

    file_name = cdt + ".txt"
    return file_name

def attach_period():
    pass
def save_sentences():
    pass
    

def append_multiple_lines(file_name, lines_to_append):
    # Open the file in append & read mode ('a+')
    
    # if not os.path.exists(file_name):
        # might need to the folder
        # os.chdir(path)
        
        # get current working directly
        # os.getcwd()
        
        # if the demo_folder directory is not present 
        # then create 
        # os.mkdir
        
        # os.makedirs("path/to/somewhere/filename")
        
        #os.chdir to the directly just created abobe
        
    with open(file_name, "a+",encoding="UTF-8") as file_object:
        appendlines = False
        # Move read cursor to the start of file.
        file_object.seek(0)
        # Check if file is not empty
        data = file_object.read(100)
        if len(data) > 0:
            appendlines = True
        # Iterate over each string in the list
        for line in lines_to_append:
            # If file is not empty then append '\n' before first line for
            # other lines always append '\n' before appending line
            if appendlines == True:
                file_object.write("\n")
            else:
                appendlines = True
            # Append element at the end of file
            file_object.write(line)
            
file_name = get_file_name()

lines = ["こんにちは"]
append_multiple_lines(file_name, lines)

os.remove("0623-1820.txt")