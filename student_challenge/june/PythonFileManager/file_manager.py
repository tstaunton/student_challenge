# June Student Challenge

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
