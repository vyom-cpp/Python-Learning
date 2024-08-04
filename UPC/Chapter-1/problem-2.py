import os

directory_path = 'D:\FCC-JS\JS_Modules'

contents = os.listdir(directory_path)

for item in contents:
    print(item)
