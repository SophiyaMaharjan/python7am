class Calculator:
    ## the function that start and ends with double underscore is called dunder
    def __init__(self, p, t, r):
        # self.p = p
        # self.t = t
        # self.r = r
        self.result = [p,t,r]
        pass

    def calvalue(self):
        # self.result = (self.p*self.t*self.r)/100
        self.results = self.result[0]*self.result[1]*self.result[2]/100
        pass

    def display(self):
        return f'simple interest is {self.results}'
        pass

    pass

obj = Calculator(500,8,10)
# obj.takevalue()
obj.calvalue()
print(obj.display())