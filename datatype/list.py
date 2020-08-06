data = ['ram','sita', 123]
users = ['gita','sophiya','madan']
'''insert: inserts the string in the mentioned string 
where as data[1]='fgshdfg' replaces the string in that index'''
# data.insert(1,'binita')

#print(data+users)#concatinates two list
data.extend(users)#it extends the data list with users list

print(data)

# users.sort(reverse=True) #it reverse the list in descending order if false written then in ascending order

# total = len(users)
# x=0
# while x<total:
#     print(users[x])
#     x+=1

#print(dir(data))