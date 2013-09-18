import setup

setup.connect_to('test1')

from user_data.score.info import HISTORY_INFO
from model.category import HARMONIZED_CATEGORIES, BLACK_LIST

f = open('cuisines_formatted.txt')
f2 = open('category_mapping.csv', 'w')

cuisines = {}

for line in f.readlines():
    cuisines[line.split(':')[0].strip().lower()] = int(line.split(':')[1].strip())

blacklisted = []

for cuisine, count in cuisines.iteritems():
    if cuisine in BLACK_LIST:
        blacklisted.append(cuisine)
    #if not cuisine in HISTORY_INFO and not cuisine in BLACK_LIST:
    #    print cuisine

print blacklisted
print len(blacklisted)
'''

for cuisine, count in cuisines.iteritems():
    #if cuisine in HARMONIZED_CATEGORIES:
    if not cuisine in BLACK_LIST:
        print >>f2, cuisine + ',' + HARMONIZED_CATEGORIES[cuisine]['category'].name + ',' + HISTORY_INFO[cuisine]  +',' + str(count)

f2.close()
'''
