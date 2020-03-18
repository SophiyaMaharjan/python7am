# try:
#     print(10/0)
# except Exception as e: #holds the error in the variable e
#     print(e)
# finally:        #this is run at the last of the program whether the program gives error or not
#     print('Done')

''' raise doenot have return type it is itself a return type raise is used to create a custom error'''

def add(x,y):
    if y==0:
        raise Exception('y is zero')
    return x/y

try:
    add(20,0)
except Exception as error:
    print(error)