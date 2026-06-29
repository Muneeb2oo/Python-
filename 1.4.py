import os

# '.' means current directory
directory = '.'

# Get the list of files and folders
contents = os.listdir(directory)

# Print them one by one
print("Contents of the directory:")
for item in contents:
    print(item)
