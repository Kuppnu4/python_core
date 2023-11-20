def get_recipe(path, search_id):
    
    with open(path, 'r') as recipes:
        while True:
            dish = recipes.readline()
            if not dish:
                break
            else:
                
                dish = dish.removesuffix('\n').split(',')
                if search_id == dish[0]:
                    recipe = {}
                    recipe['id'] = dish[0]
                    recipe['name'] = dish[1]
                    recipe['ingredients'] = dish[2:]
                    return recipe

                else:
                    return None

            







path = 'recipes'
print(get_recipe(path, '60b90c1c---13067a15887e1ae1'))
