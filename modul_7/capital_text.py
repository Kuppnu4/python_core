def capital_text(s):
    capital_flag = True
    new_s = ''
    
    for i in s:
        if i == ' ':
            new_s += i
            continue
        elif i == '.' or i == '!' or i == '?':
            capital_flag = True
            new_s += i
            continue
        elif capital_flag:
            i = i.upper()
            new_s += i
            capital_flag = False
        else:
            new_s += i
            
            
            
    return(new_s)





print(capital_text('alert. boss! oh'))
