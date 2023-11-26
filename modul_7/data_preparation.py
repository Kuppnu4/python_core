def data_preparation(list_data):

    new_list = []
    for i_list in list_data:
        if len(i_list) > 2:
            i_list.remove(min(i_list))
            i_list.remove(max(i_list))
        new_list.extend(i_list)

    
    new_list.sort(reverse=True)
    print(new_list)


data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]])
          

