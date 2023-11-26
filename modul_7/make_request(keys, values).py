def make_request(keys, values):
    
    request = {}
    
    if len(keys) != len(values):
        return {}

    for i in range(len(keys)):
        request[keys[i]] = values[i]

    return request
    
