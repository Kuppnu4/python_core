def all_sub_lists(data):
    new_list = [[]]
    j = 0
    for i in range(len(data) + 1):
        
        for d in data:
            j+=1
            print(j, '<<<<>>>>', i)
            if len(data[j-1:j+i]) <= i:
                continue
            new_list.append(data[j-1:j+i])
            
            print(new_list)
        j = 0


    print(new_list)
    return(new_list)
    



all_sub_lists([0, 1, 1, 2])
