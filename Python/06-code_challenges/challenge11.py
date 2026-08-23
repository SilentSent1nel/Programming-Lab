my_list = []

def append_size(my_list):
    list_length = len(my_list)
    my_list.append(list_length)
    return my_list

print(append_size([23, 42, 108]))