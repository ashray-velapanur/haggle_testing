import json
from category import HARMONIZED_CATEGORIES
from category import BLACK_LIST

file = open('vendors_test1')

vendors = []
unmapped_cuisines = set()
wrongly_mapped_vendors = [] 

for line in file.readlines():
    vendor_dict = {}
    vendor_dict['id'] = line.split(',')[1]
    vendor_dict['haggle_cuisine'] = line.split(',')[0]
    vendor_dict['third_party_cuisine'] = line.split(',')[2].strip().lower()
    vendors.append(vendor_dict)

for vendor in vendors:
    if vendor['third_party_cuisine'] in BLACK_LIST:
        continue
    if not vendor['third_party_cuisine'] in HARMONIZED_CATEGORIES:
        unmapped_cuisines.add(vendor['third_party_cuisine'])
        continue
    if not HARMONIZED_CATEGORIES[vendor['third_party_cuisine']]['category'].name == vendor['haggle_cuisine']:
        wrongly_mapped_vendors.append(vendor)

print unmapped_cuisines
print wrongly_mapped_vendors

