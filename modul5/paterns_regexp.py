import re
from re import search, findall, sub

url_regexp = r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]+)'

result = search(url_regexp, 'https://www.google.com')
print(result)
print(result.group())


result = findall(url_regexp, 'https://www.google.com dadadadad http://www.fhfhfh.ccc')
print(result)


ip_regexp = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
print(findall(ip_regexp, '127.123.124.125 172.173.174.175'))


c = sub(ip_regexp, '*', '127.123.124.125 asd 172.173.174.175 dsa')
print(c)
