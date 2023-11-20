def encrypt(b_obj, key):

    b_obj_array = bytearray(b_obj)

    for i, b in enumerate(b_obj_array):
        n = b + key
        
        if n > 255:
            n -=255
            
        b_obj_array[i] = n

    return b_obj_array


def decrypt(b_obj, key):
    b_obj_array = bytearray(b_obj)

    for i, b in enumerate(b_obj_array):
        n = b - key
        
        if n < 255:
            n +=255
            
        b_obj_array[i] = n
        
    return b_obj_array


if __name__ == '__main__':
    pwd = input('Enter your password: ')
    encrypted_pwd = encrypt(pwd.encode(), 200)

    with open('password.txt', 'wb') as file:
        file.write(encrypted_pwd)

    with open('password.txt', 'rb') as file:
        encrypted_pwd = file.read()
        print(encrypted_pwd)

    print(decrypt(encrypted_pwd, 200))
    
#pwd = b'password'
#key = 5
