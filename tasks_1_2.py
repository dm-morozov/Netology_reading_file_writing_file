from pprint import pprint


class CookBook:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def read_file(self):
        cook_book = {}
        with open(self.file_name, 'r', encoding='utf-8') as file:
            recipe_name = ''
            ingredients_count = 0
            for line in file:
                line_stripped = line.strip()
                if line_stripped:
                    if not recipe_name:
                        recipe_name = line_stripped
                        # cook_book[recipe_name] = []
                    elif not ingredients_count:
                        ingredients_count = int(line_stripped)
                    else:
                        ingredients_info = line_stripped.split('|')
                        if len(ingredients_info) == 3:
                            ingredient = {
                                'ingredient_name': ingredients_info[0].strip(),
                                'quantity': int(ingredients_info[1]),
                                'measure': ingredients_info[2].strip()
                            }
                            cook_book.setdefault(recipe_name, []).append(ingredient)
                            if len(cook_book[recipe_name]) == ingredients_count:
                                recipe_name = ''
                                ingredients_count = 0
        return cook_book


def get_shop_list_by_dishes(dishes, person_count = 1):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                ingredient_name = ingredients.get('ingredient_name')
                measure = ingredients.get('measure')
                quantity = ingredients.get('quantity')
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                        'measure': measure,
                        'quantity': quantity * person_count
                    }        
    return shop_list


recipes = CookBook('recipes.txt')
cook_book = recipes.read_file()
# pprint(cook_book)

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(shop_list)
