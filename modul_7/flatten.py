
def flatten(data):
    new_list = []
    
    for d in data:
        if type(d) == int:
            
            new_list.append(d)
            
        else:
            new_list.extend(flatten(d))

    return new_list
            
            
            

    
        
print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]] ))
