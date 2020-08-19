
# the name of class is same as the file name
# the function inside the class is called method and behaviour of class

class Students:
    x = 10  # this is the property or attribute of the class
    def __init__(self,name):
        self.name = name

    def test(self):
        print(self.x)#self represents class itself
        pass

    def getfullname(self):
        return f'your name is {self.name}'
        pass
    pass

obj = Students('ram') #it is not necessary to keep paranthesis

obj.getfullname()
