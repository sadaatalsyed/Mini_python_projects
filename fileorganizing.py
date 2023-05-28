import os,shutil
from pathlib import Path   

for folderName, subfolders, files in os.walk('F:\Study Related\Python_Projects_begginer_level\Data Analysis'):

    print("The current folder is "+folderName)
    for subfolder in subfolders:
        print('Subfolder of '+folderName+': '+subfolder)
    for filename in files:
        print('File inside '+ folderName+ ': '+filename)
    
    print(' ')