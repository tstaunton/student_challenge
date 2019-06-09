# June Student Challenge

# Import necessary modules.
# The OS and Subprocess modules deal with the operating system
import shutil        
import os        
import time
import subprocess

def Read():       
    path=input("Enter the file path to read:")
    file=open(path,"r")
    print(file.read()) 
    input('Press Enter...')  
    file.close() 


def Write():    
    path=input("Enter the path of file to write or create:")
    if os.path.isfile(path):
        print('Rebuilding the existing file') 
    else:
        print('Creating the new file') 
    text=input("Enter text:")
    file=open(path,"w")
    file.write(text)
