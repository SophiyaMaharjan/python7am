'''open : if file exists opens that file else create that file'''
# try:
#     handle=open('students.txt','a',encoding='utf-8') #encoding='utf-8' is not necessary to define it takes it by default
#     handle.write('hello python file handling 3')
# except Exception as error:
#     print(error)
# finally:
#     handle.close()

# hand = open('students.txt','r')
# # print(hand.read())
# print(hand.readline())#reads first line only
# print(hand.readlines())#reads all the data and converts into list form
# print(hand.readable()) # checks whether the file is in readable mode or not
# hand.close()

'''to remove the file we need to import os to get the path of the file
it deletes the file inside the existing project folder only'''

import os

# os.remove('students.txt')#deletes the file named students.txt

# os.rmdir('users') #removes the directory named users

if not os.path.exists('record.txt'):
    file = open('record.txt','w')
    file.close()