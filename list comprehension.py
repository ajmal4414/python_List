# fruits=["apple","orange","kivi"]
# newlist=[]
# for x in fruits:

#list comprehension number prime or not
# prime=[x for x in range(2,20)
#        if all (x%y!=0
#                for y in range(2,x))]
# print(prime)






#list comprehension number prime or not
# prime=[x for x in range(2,20)if all (x%y!=0 for y in range(2,x))]
# print(prime)

#nestedloop comprhension
list1=[2,4,6]
list2=[8,10,12]
comblist=[(x,y)for x in list1 for y in list2]
print(comblist)

#listcomprehension using factorial no