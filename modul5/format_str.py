'{0} {1} {2} {3}'.format('a', 'b', 'c', 'd')
'{name} {last_name}'.format(name = 'Nick', last_name = 'Smith')

'{:d}'.format(10)
'10'
'{:b}'.format(10)
'1010'

'{0:d} {0:#b}'.format(10)
'10 0b1010'
'{0:d} {0:#b} {0:#x}'.format(10)
'10 0b1010 0xa'
a = 10
f'{int(a)},{bin(a)}, {hex(a)}'
'10,0b1010, 0xa'
'{0:*^10}'.format(10)
'****10****'
'{0:*<10}'.format(10)
'10********'
'{0:*>10}'.format(10)
'********10'
