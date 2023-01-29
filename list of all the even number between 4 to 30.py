#6.generate a python list of all the even numbers between 4 to 30
list=[]
def even(x,y):

    for i in range(x,y,2):
        list.append(i)
    print(list)

even(4,30)
