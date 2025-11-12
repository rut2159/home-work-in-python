import os
from fileinput import close

#ex 1
folder_name = "MyNewFolder"
# os.mkdir(folder_name)
folder_path = "Z:\יד תשפו\וסרמן רות\python\שעורי בית\PythonProject\MyNewFolder"
#ex 2
if os.path.isdir(folder_path) and not os.listdir(folder_path):
    try:
        os.rmdir(folder_path)
        print(f"Empty folder '{folder_name}' deleted successfully.")
    except OSError as e:
        print(f"'{folder_name}' is not an empty folder or does not exist: {e}")
#ex 4,3
new_file="my_new_file.txt"
file=os.path.join(folder_path,new_file)
with open(file,"w") as file:
    file.write("this is new file in new folder")
#ex 5
file_to_delete="my_new_file.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"file :{file_to_delete} deleted successfully")
else:
    print(f"file :{file_to_delete} does not deleted")

#ex 6
list="Z:\יד תשפו\וסרמן רות\python\שעורי בית\PythonProject\lesson5.py"
if os.path.exists(list):
    print(f"content of: {list}:{os.listdir('.')}")
else:
    print("directory not found")
#ex 7
print(f"the current working directory is:{os.getcwd()}")


