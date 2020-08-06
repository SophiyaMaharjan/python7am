#decorator

# def getdoc(anyfunction):
#     def inner():
#         return(anyfunction.__doc__)
#     return inner()

# @getdoc

def zero_check(function):
    def check(x,y):
        if x ==0 or y==0:
            msg = "pass the value greater than zero"
            return msg
        return function(x,y)
    return check
pass

def hundred_check(anyfunction):
    def check_hun(a,b):
        if a>99 or b>99:
            msg2 = "you have entered the value above 99"
            return 
        return anyfunction(a,b)
    return check_hun
pass

@zero_check
@hundred_check
def add(x,y):
    return x+y
pass

print (add(1000,0))