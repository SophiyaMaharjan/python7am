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

def login():
    username = input("entere uname :")
    password = getpass.getpass("enter password")
    get_users_data = open('record.txt','r').readlines()
    user = []
    print (user)
    for user in get_users_data:
        users.append(user.split())
    total_users = len(users)
    print(total_users)
    increment = 0
    login_success = 0
    while increment< total_users:
        get_username = users[increment][0]
        get_password = users[increment][1]
        if username == get_username and password == get_password:
            login_success =1
        increment +=1
    
    if login_success == 1:
        print('welcome'+username)
    else:
        print("username and password not match")

message = input("Do you have an account y/n : ")

if message == 'y':
    login()
else:
    register()