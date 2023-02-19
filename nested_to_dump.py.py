import os
import shutil

#add source folder with all the folders (nested)
source_folder_input=input("enter source folder :") + "\\"
source_folder=source_folder_input
#add destination folder
destination_folder_input=input("enter destination folder :") + "\\"
destination_folder=destination_folder_input


for file_name1 in os.listdir(source_folder):
    file_name = source_folder + file_name1 + "\\"
    for file_name2 in os.listdir(file_name):
        source=file_name + file_name2
        destination= destination_folder + file_name2 

        if os.path.isfile(source):
            shutil.copy(source,destination)
            print("File Copied =",file_name2)
