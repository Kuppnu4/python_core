2 ** 3
    2 * 2 ** 2
        2 * 2 ** 1
            2 * 2 ** 0

def recurs(x, n):
    
    if n == 0:
        return 1
    
    return x * result(x, n-1)
    

recurs(2, 3)
    2 * recurs(2, 2)
        2 * recurs(2, 1)
            2 * recurs(2, 0)
                1
            
