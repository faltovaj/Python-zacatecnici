import os

print('Adresar: ', os.getcwd())
print('List adresar: ', os.listdir())

path = os.getcwd()
for folder_path, folders, files in os.walk(path):
    print(folder_path)
    print(folders)
    print(files)

# How many folders
# How many files are in the current directory?
# Count python files only

# Global path: vypis souboru
import glob
path = os.getcwd() + '//*'    #// na konci nutne!!!! Pozor: windows \\!!!
#path = os.getcwd() + '//*.py' #pouze Python files
for filepath in glob.glob(path):
    print('Filepath (glob)', filepath)

#Rekurzivni prohledavani
path = os.getcwd()+'//**//*'
for filepath in glob.glob(path, recursive=True):
    print(filepath)

# Make a new directory
os.mkdir('new_dir')
os.rename('README_2019.txt','README_2019_renamed.txt')
