def get_cats_info(path):
    cats_list = []
    with open(path, 'r') as cats_base:
        while True:
            cat_info = {}
            cat_line = cats_base.readline().removesuffix('\n')
            if not cat_line:
                break
            else:
                cat_info_list = cat_line.split(',')
                cat_info['id'] = cat_info_list[0]
                cat_info['name'] = cat_info_list[1]
                cat_info['age'] = cat_info_list[2]
                cats_list.append(cat_info)
                
    print(cats_list)


path = 'data_base'
get_cats_info(path)
