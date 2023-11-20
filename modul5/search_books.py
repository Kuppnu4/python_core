articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def check_key(string_pattern, key):

    print(string_pattern, '     >>>', key)
    
    if string_pattern.find(key) != -1:
        return True
    else:
        return False
        
            

def find_articles(key, letter_case=False):
    new_dict= []
    serch_parameters = ['title', 'author']
    
    
    for book in articles_dict:
        
        if letter_case:

            for param in serch_parameters:
                if check_key(book[param], key):
                    new_dict.append(book)

        else:

            for param in serch_parameters:
                if check_key(book[param].lower(), key.lower()):
                    new_dict.append(book)


    return new_dict


print(find_articles('The', True))
