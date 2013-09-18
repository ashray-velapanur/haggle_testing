import sys

sys.path.append('../')

import setup

setup.run()

from model.category import HARMONIZED_CATEGORIES 
from user_data.score.info import HISTORY_INFO

mappings = []

mappings.append({'third_party_category': 'third_party_category', 'haggle_category': 'haggle_category', 'history_score_copy': 'history_score_copy'})

for k, v in HARMONIZED_CATEGORIES.iteritems():
    mapping_dict = {}
    mapping_dict['third_party_category'] = k
    mapping_dict['haggle_category'] = v['category'].name
    mapping_dict['history_score_copy'] = HISTORY_INFO[k]
    mappings.append(mapping_dict)

with open('category_mapping.csv', 'w') as f:
    for mapping in mappings:
        print >>f, mapping['third_party_category'] + ',' + mapping['haggle_category'].lower() + ',' + mapping['history_score_copy']
