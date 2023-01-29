#zip method
# name=["akhil","john","roy"]
# age=[12,34,45]
# c=zip(name,age)
# print(list(c))
#enumerate
# fo
# name=["akhil","john","roy"]
# age=[12,34,45]
# for i,(name,age)   in enumerate (zip(name,age)):
#     print(i,name ,age)

#mapping#list of strings
# l=['john','sajin','tom']
# c=list(map(list,l))
# print(c)

#unzip
# name=["sajin","tom","john"]
# age=[23,54,23]
#
# c=zip(name,age)

# a=5
# b=7
# def sum


# fuction list

# def list_add():
#     print("append a value:",list1.append(10))
# list1=[2,4,6,8,]
# list_add=(list1.append)

# return function

# def sum():
#     a=30
#     b=55
#     c=a+b
#     return c
#
# print("the sum is:",sum())

# returning sum function
# def sum():
#     a=100
#     b=100
#     c=a+b
#     return c
# print("the sum is:",sum())

# append function
# def change_list(list1):
#     list1.append(40)
#     list1.append(30)
# list1=[20,50,60]
# change_list(list1)
# print("list outside function is",list1)

#largest number find using function

# def max(list1):
#     list1=[20,40,50,100]
#
# max(list1)
# print("largest num is:", list1)

#largets number using max function

list1=[20,60,50,5]
def max_num_in_list(list1):
    max=list1[0]
    for a in list1:
        if a> max:
            max=a
    return max
print(max_num_in_list([20,60,50,5]))




