import os
import getpass

def login():
    uname = input("enter user name : ")
    psw = getpass.getpass('enter password :')
    
    with open('record.txt','r') as file:
       # data = obj.readlines()
        logged = False
        for row in file:
            column = row.split()
            username = column[0]
            password = column[1]
            if username == uname and password == psw:
                logged = True
                print('hello,f{uname}\n you have sucessfully logged in')
                exit()
            else:
                continue
                
    if not logged:
        print('username or password wrong')
    

login()