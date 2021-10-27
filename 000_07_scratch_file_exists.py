import os.path

# os.path.exists()
# os.path.isdir()

if os.path.isfile("COMMANDS.txt"):
    print("File exists")
else:
    print("File doesn't exist")


## pathlib2 python lib required
# from pathlib import Path
#
# if Path('filename.txt').is_file():
#     print ("File exist")
# else:
#     print ("File not exist")
