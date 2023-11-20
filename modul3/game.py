import random

SIZE_X = random.randint(5,20)
SIZE_Y = random.randint(5,20)

pos_x = random.randint(0, SIZE_X)
pos_y = random.randint(0, SIZE_Y)

def map_generate():
    
    for m in range(SIZE_X):
        line  = "|"
        for n in range(SIZE_Y):
            if pos_x == m + 1 and pos_y == n + 1:
                line += "X|"
            else:
                line += " |"
        print(line)

print(SIZE_X, SIZE_Y)
print(pos_x, pos_y)
map_generate()

