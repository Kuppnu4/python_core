str = 'Hello world'

str.capitalize() # первое слово пишет с большой буквы

str.casefold() #делает то же что и lowercase(), но не только для букв, 
                #а и для иероглифов, для нормализации строки для сравнения и хранения

str.center(10, '*') #для форматирования и центрования строки,
                    #пустые места заполняются '*'

str.encode()

str.endswith(start, end) #не обязательно с начала и до конца строки
str.startswith(start, end)

str.find('lo')#возвращает индекс вхождения элемента в подстроку
            #если вхождения нет возвращает -1

str.index('z')#возвращает индекс вхождения элемента в подстроку
            #если вхождения нет возвращает ошибку


str.isalnum()
str.isalpha()
str.isidentifier()
str.islower()
str.isspace()
str.istitle()
str.isupper()

str.join('*')#соедтняет строки через символ '*'

str.strip()#убирает пробелы

str.partition('sep')#разделяет по сепаратопу но не игнорирует его

str.rsplit()

str.swapcase()


