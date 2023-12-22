# question 1
# Function sum()
def sum(list):
    # set total sum = 0
    total_sum = 0
    for i in list:
        # Adding (total_sum = total_sum + i)
        total_sum += i
    return total_sum

print(sum([1, 2, 3]))

#ques 2
def multiple(lists):
    total_num = 1
    for i in lists:
        total_num = total_num * i 
    return total_num

print(multiple([2, 3, 4]))

#ques 3
def numb(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

print(numb([5, 7, 3, 9]))
    
#ques 4
def same_count(list):
    qwedf4crf-[=]
