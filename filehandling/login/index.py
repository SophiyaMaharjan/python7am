import os
import getpass

if not os.path.exists('record.txt'):
    file = open('record.txt','w')
    file.close()

def register():
    username = input('Enter username : ')
    if username in open('record.txt','r').read():
        print ('username already exists')
        message = input('Do you want to continue y/n: ')
        if message == 'y':
            register()
            exit()
        else:
            exit()  # it exits the loop
    password = getpass.getpass('Enter a password : ')
    confirm_password = getpass.getpass('Enter confirm password')
    if password != confirm_password:
        print('your password does not match')
        exit()
    
    try:
        handle = open('record.txt','a')
        handle.write(username)
        handle. write(" ")
        handle.write(password)
        handle.write('\n')
    except Exception as error:
        print(error)
    finally:
        handle.close()
register()