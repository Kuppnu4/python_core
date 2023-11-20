import base64

def save_credentials_users(path, users_info):
    
    with open(path, 'wb') as credentials:
        for k, v in users_info.items():
            credentials.write(k.encode() + b':' + v.encode() + b'\n')



def get_credentials_users(path):
    
    with open(path, 'rb') as credentials:

        users_info = credentials.read().decode()
        users_list = users_info.removesuffix('\n').split('\n')

        print(users_list)
        return users_list
        


def encode_data_to_base64(data):
    encoded_data = []
    for user in data:
        byte_user = user.encode('utf-8')
        base64_encode = base64.b64encode(byte_user)
        base64_user = base64_encode.decode('utf-8')
        encoded_data.append(base64_user)
    return(encoded_data)
        
    


data = ['andry:uyro18890D', 'steve:oppjM13LL9e']
path = 'output'
users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
#get_credentials_users(path)
print(encode_data_to_base64(data))

