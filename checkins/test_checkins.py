import json
from category import BLACK_LIST
import datetime

DEPRECIATION_YEARLY = .8
DEPRECIATION_MONTHLY = DEPRECIATION_YEARLY ** (1.0 / 12)

USER = 'resnick.matthew@gmail.com' 

json_files = ['checkins_json_1', 'checkins_json_2', 'checkins_json_3', 'checkins_json_4', 'checkins_json_5']
db_file = 'checkins_test1'

total_checkins = 0.0
checkins = []
blacklisted_checkins = []
valid_checkins = []
valid_checkin_ids = []
db_checkins = []
db_checkin_ids = []

def months_between(start, end):                                                                                                                                                                                
      return (end.year - start.year) *  12 + end.month - start.month

def is_invalid_category(category):
    return category.lower() in BLACK_LIST if category else True

def get_checkins(checkins_json):
    for checkin in checkins_json:
        checkin_dict = {}
        checkin_dict['name'] = checkin['venue']['name']
        checkin_dict['id'] = checkin['id']
        checkin_dict['created_at'] = checkin['createdAt']
        categories = checkin['venue']['categories']
        checkin_dict['category'] = categories[0]['name'].lower().encode('utf-8') if len(categories) > 0 else ''
        for category in categories:
            if 'primary' in category and category['primary']:
                checkin_dict['category'] = category['name'].lower()
        checkins.append(checkin_dict)
        if is_invalid_category(checkin_dict['category']):
            blacklisted_checkins.append(checkin_dict)
        else:
            valid_checkin_ids.append(checkin_dict['id'])
            valid_checkins.append(checkin_dict)

for file in json_files:
    with open(file) as f:
        response = json.load(f)
        checkins_json = response['response']['checkins']['items']
        get_checkins(checkins_json)

with open(db_file) as f:
    for line in f.readlines():
        checkins_dict = {}
        user = line.split(',')[4]
        network = line.split(',')[1]
        if user == USER  and network == '4S':
            checkins_dict['id'] = line.split(',')[3]
            checkins_dict['vendor_id'] = line.split(',')[0]
            db_checkins.append(checkins_dict)
            db_checkin_ids.append(line.split(',')[3])

for checkin in valid_checkins:
    total_checkins += 1.0 *  DEPRECIATION_MONTHLY ** months_between(datetime.datetime.fromtimestamp(checkin['created_at']), datetime.datetime.now())

print 'weighted checkins: ' + str(total_checkins), 'blacklisted: ' + str(len(blacklisted_checkins)), 'valid: ' + str(len(valid_checkins)), 'total: ' + str(len(checkins))

print '\ncheckins from json not in db'
for checkin in valid_checkins:
    if not checkin['id'] in db_checkin_ids:
        print checkin 

print '\ncheckins from db not in json'
for checkin in db_checkins:
    if not checkin['id'] in valid_checkin_ids:
        print checkin


