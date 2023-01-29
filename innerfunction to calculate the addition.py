#create inner function to calculate the addition
num1=int(input("enter the 1st number:"))
num2=int(input("enter the 2nd number:"))

def outer(x,y):
    add=x+y
    def inner(x,y):
        return add
    inner(num1,num2)
    print('add:',add)
    result=add+5
    return result

print('add+5:',outer(num1,num2))