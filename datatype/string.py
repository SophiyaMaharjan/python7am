#message ='we are learning python list'
# print(dir(message))
'''makes the message capitlized'''
# print(message.title())

# '''changes the message into upper case'''
# print(message.upper())

# print(message.count(message))

username = 'hello admin'

x= username.replace('admin','ram') #replace the word admin by ram
#print(x)
message ='     Hello python we are learning python'
#print(message.count('python')) # counts the number of word python in sentence

#print(message.lstrip())#removes the unecessary space from the system except space between two txt

'''if the text is not found the returns -1 else returns the position of the particular string'''
# print(message.find('we')) 
'''display the position of the string if the string is present else throws an error'''
# print(message.index('are'))
'''it just add the string randomly'''
# print(message.join('>>'))

'''it splits the sentence into list '''
print(message.split('p'))