def formatted_numbers():
    table = []
    table.append('|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary'))
    for n in range(16):
        table.append('|{:<10d}|{:^10x}|{:>10b}|'.format(n, n, n))
    
    for i in table:
        print(i)

formatted_numbers()
