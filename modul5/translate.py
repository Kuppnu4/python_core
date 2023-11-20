translate_map = {ord('є'): 'ie', ord('і'): 'y'} #ord показывает номер символа в таблице ASCII

str = 'пєльмєні'.translate(translate_map) #пieльміенy

print(str)
