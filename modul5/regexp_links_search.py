import re


def find_all_links(text):
    result = []
    
    iterator = re.finditer("http(?:|s)://\w+\.?\w+\.[a-zA-Z]{3}", text)
    for match in iterator:
        result.append(match.group())
    return result

text = 'htttp://jfjfjf.com jjkfk 12 lkfdldj 34lkfsllk '\
       'http://jfjf.kfk kfkfkfk kfkfk 12 kfkf 21 http://kfkfkfk '

print(find_all_links(text))
