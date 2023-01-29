#2.programme to reverse a string
def reverse(str1):
    res=""
    for i in str1:
      res=i+res
    return res
str1 = "1234abcd"
print(reverse(str1))




