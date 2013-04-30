from category import HARMONIZED_CATEGORIES

with open('category_mapping.csv', 'w') as file:
    for category in HARMONIZED_CATEGORIES:
        print >> file, category.encode('utf-8') + ',' + HARMONIZED_CATEGORIES[category]['category'].name

