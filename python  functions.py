#largets number using max function

list1=[20,60,50,5]
def max_num_in_list(list1):
    max=list1[0]
    for a in list1:
        if a> max:
            max=a
    return max
print(max_num_in_list([20,60,50,5]))
