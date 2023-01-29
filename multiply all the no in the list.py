#1.multiply all the no in the list
list1=[2,4,6]
list2=[4,2,2]


def multiply(list):
    result=1
    for x in list:
        result=result*x
    return result

print(multiply(list1))
print(multiply(list2))