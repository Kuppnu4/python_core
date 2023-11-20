
import sys


def parse_args():
    result = ""
    for arg in sys.argv[1:]:
        if arg == sys.argv[-1]:
            result += f'{arg}'
            break
        result += f'{arg} '
    
    
        
            
        
    return result

print(parse_args())
