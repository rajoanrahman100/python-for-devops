from pathlib import Path

# Create a Path object
pathOne=Path("path-directories") # Path object for a directory
print(pathOne.exists()) # check if the directory exists

for file in pathOne.glob("*.py"):
    print(file) # print all the python files under the 'path-directories' directory
 
# pathOne.rmdir() # remove the directory

# Get the current directory
current_directory = Path.cwd()
print(current_directory)
