cook_book = {}

with open('recipes.txt', encoding='utf-8') as file:
    all_lines = file.read().split('\n\n')
    for food in all_lines:
        kind_of_food, n, line = food.split('\n', 2)
        cook_book.setdefault(kind_of_food, [])
        for parts in line.split('\n'):
            ingredient_name, quantity, measure = parts.split(' | ')
            dct = {
                   'ingredient_name': ingredient_name,
                   'quantity': int(quantity),
                   'measure': measure
            }
            cook_book[kind_of_food].append(dct)



def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            ingredient_name = ingredients['ingredient_name']
            if res.get(ingredient_name, None) is None:
                res[ingredient_name] = {'measure': ingredients['measure'], 'quantity': ingredients['quantity'] * person_count}
            else:
                res[ingredient_name]['quantity'] += ingredients['quantity'] * person_count
    return res


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))