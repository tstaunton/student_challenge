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

def Add():      
    path=input("Enter the file path:")
    text=input("Enter the text to add:")
    file=open(path,"a")
    file.write('\n'+text)


def Delete():          
    path=input("Enter the path of file for deletion:")
    if os.path.exists(path):     
        print('File Found')     
        os.remove(path)          
        print('File has been deleted')
    else:
        print('File Does not exist')  


def Dirlist():      
    path=input("Enter the Directory path to display:")
    sortlist=sorted(os.listdir(path))       
    i=0
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1

def Check():       
    fp=int(input('Check existence of \n1.File \n2.Directory \n'))
    if fp==1:
        path=input("Enter the file path:")
        os.path.isfile(path)
        if os.path.isfile(path)==True:
            print('File Found')
        else:
            print('File not found')
    if fp==2:
        path=input("Enter the directory path:")
        os.path.isdir(path)
        if os.path.isdir(path)==False:
            print('Directory Found')
        else:
            print('Directory Not Found')


def Move():        
    path1=input('Enter the source path of file to move:')
    mr=int(input('1.Rename \n2.Move \n'))
    if mr==1:
        path2=input('Enter the destination path and file name:')
        shutil.move(path1,path2)
        print('File renamed')
    if mr==2:
        path2=input('Enter the path to move:')
        shutil.move(path1,path2)
        print('File moved')


def Copy():       
    path1=input('Enter the path of the file to copy or rename:')
    path2=input('Enter the path to copy to:')
    shutil.copy(path1,path2)
    print('File copied')


def Makedir():            
    path=input("Enter the directory name with path to make \neg. C:\\Hello\\Newdir \nWhere Newdir is new directory:")
    os.makedirs(path) 
    print('Directory Created')


def Removedir():             
    path=input('Enter the path of Directory:')
    treedir=int(input('1.Deleted Directory \n2.Delete Directory Tree \n3.Exit \n'))
    if treedir==1:
        os.rmdir(path)
    if treedir==2:
        shutil.rmtree(path)
        print('Directory Deleted')
    if treedir==3:
        exit()


def Openfile():
    path=input('Enter the path of program:')
    try:
        os.startfile(path)
    except:
        print('File not found')

run=1
while(run==1):
    try:
        os.system('clear')
    except OSError:
        os.system('cls')        
    print('\n########## Python File Manager ##########\n')
    print('The current time and date is:',time.asctime())
    print('\nChoose the option number: \n')
    dec=int(input('''1.Read a file
2.Write to a file
3.Append text to a file
4.Delete a file
5.List files in a directory
6.Check file existence
7.Move a file
8.Copy a file
9.Create a directory
10.Delete a directory
11.Open a program
12.Exit

'''))
    if dec==1:
        Read()
    if dec==2:
        Write()
    if dec==3:
        Add()
    if dec==4:
        Delete()
    if dec==5:
        Dirlist()
    if dec==6:
        Check()
    if dec==7:
        Move()
    if dec==8:
        Copy()
    if dec==9:
        Makedir()
    if dec==10:
        Removedir()
    if dec==11:
        Openfile()
    if dec==12:
        exit()
    run=int(input("1.Return to menu\n2.Exit \n"))
    if run==2:
        exit()
