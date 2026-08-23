my_list = []
new_list = []

def odd_indices(my_list):
    for index in range (1, len(my_list), 2):
        new_list.append(my_list[index])
    return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))