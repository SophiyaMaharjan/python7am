# def take_value():
#     x = int(input('enter a p '))
#     y = int(input('enter time '))
#     z = int(input('enter rate '))
#     return [x,y,z]

# def calculate():
#     data = take_value()
#     p = data[0]
#     t = data[1]
#     r = data[2]
#     return p*t*r/100

# def display():
#     print(calculate())

# display()

#nested function
# def  users():
#     def names(name):
#         return f'your name is {name}'
#     return names
# data = users()
# print (data('ram'))

#function scope

# x = 10
# def test():
#     global x  # to call variable outside the function with same variable name
#     x=x+20
#     print(x)
# test()

# anonymous function lamda

# data = lambda x,y : x+y
# print(data(10,20))

# def users(x):
#     return lambda y : x+y

# a= users(10)
# print(a(20))

