# def get_doc(anyfunction):
#     def inner():
#         return f'{anyfunction.__doc__}'
#     return inner

# @get_doc
# def test():
#     """this is test function"""
#     pass
# print(test())

def validation(function):
    def check(x, y):
        if x==0:
            return f"x is zero"

        return function(x, y)

    return check

@validation
def add(x, y):
    return x + y

print(add(1,4))