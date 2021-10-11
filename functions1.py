

#1 question
def count_down(num):
    new_list = []
    for i in range(num, 1, 6):
        new_list.append(i)
        return new_list
        print(count_down(5))



#2 question
def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([40,70]))

#3 question
def first_plus_length(list):
    print(list[0])
    return len(list)
print(first_plus_length([90,40,3]))


#4 question
def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []
    # greaterThan = list[1]
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([55,6,2,3,99,78,20,1]))
print(values_greater_than_second([55,0,2,3,99,78,20,1]))
print(values_greater_than_second([1]))
print(values_greater_than_second([]))