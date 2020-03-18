x=1
sum = 0
sumodd= 0
while x<=50:
    if x%2 == 0:
        sum = sum+x
    else:
       sumodd = sumodd+x
    x+=1

print('sum of even numbers {} and sum of odd numbers {}'.format(sum, sumodd))
    