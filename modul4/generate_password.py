from random import randint


def get_random_password():
    
    psw = ""
    
    for i in range(randint(6, 10)):
        psw += chr(randint(40, 126))

    return psw





def is_valid_password(password):

    length_8 = False

    if len(password) == 8:
        length_8 = True

    upper_case = False
    lower_case = False
    have_number = False

    for i in password:
        
        if i.isupper():
            upper_case = True

        if i.islower():
            lower_case = True

        if i.isnumeric():
            have_number = True
    print(length_8, "    ", upper_case, "   ", lower_case , "   ", have_number)

    return length_8 & upper_case & lower_case & have_number



def get_password():
   

    for i in range(100):
      
        print(i)
        psw = get_random_password()
        if is_valid_password(psw):
            
            return psw

    
print(get_password())
