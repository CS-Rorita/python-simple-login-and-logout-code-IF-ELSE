import time
# import only system from os 
from os import system, name

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
        
def mainMenu():
        
	print('Hi there, welcome to space account')
	print("If you don't have account, select to create new account")
	print("If you have account with us, just login with your current username and password")
	print("Create account  <1>")
	print("Login           <2>")
	print("EXIt !          <3>")
	selection=int (input(""))
	if selection==1:
		new()
	elif selection==2:
		account()
	elif selection==3:
		exit
	else:
		print ("Invalid choice,Enter 1-3")
		mainMenu()
def new():
    #  call function we defined above 
    clear() 
    print("please select a new username and password  :)")
    print("If you don't have account, select to create new account")
    nameu = input(' your new username is : \n')
    password = int(input(' your new password is : \n'))
    print(' your account has been created succesfully \n')
    print(' you will return to menu shortly  ')
    print(' please wait...  ')
    time.sleep(3) # Sleep for 3 seconds
    mainMenu()
    clear()

#main
mainMenu()
