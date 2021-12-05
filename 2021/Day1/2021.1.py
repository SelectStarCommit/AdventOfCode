file = open('input1.txt', 'r')
enumerated_data = enumerate(file.read().split())
data_list = []

for index, value in enumerated_data:
    data_list.append(str(value))
    
def depth_compare(compare_list):
    previous_depth = 0
    increase_count = 0
    
    for current_depth in compare_list:
        if int(current_depth) > int(previous_depth):
            increase_count += 1
        previous_depth = current_depth
    
    return increase_count-1
        
print('Answer 1: ', depth_compare(data_list))

def add_three_depths(x, y, z):
    three_total = 0
    three_total = three_total + int(x)
    three_total = three_total + int(y)
    three_total = three_total + int(z)
    return three_total

combined_depth = []

for i, val in enumerate(data_list):
    current_and_1 = i + 1
    current_and_2 = i + 2
    if current_and_2 > 1999 and current_and_1 == 1999:
        combined_depth.append(add_three_depths(data_list[i], data_list[current_and_1], 0))
    elif current_and_2 > 1999 and current_and_1 > 1999:
        combined_depth.append(add_three_depths(data_list[i], 0, 0))
    else:
        combined_depth.append(add_three_depths(data_list[i], data_list[current_and_1], data_list[current_and_2]))

print('Answer 2: ', depth_compare(combined_depth))