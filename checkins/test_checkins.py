import json
from category import BLACK_LIST
import datetime

json_files = ['checkins_json_1', 'checkins_json_2', 'checkins_json_3', 'checkins_json_4', 'checkins_json_5']

checkins = []
blacklisted_checkins = []
valid_checkins = []

def is_invalid_category(category):
    return category.lower() in BLACK_LIST if category else True

def get_checkins(checkins_json):
    for checkin in checkins_json:
        checkin_dict = {}
        checkin_dict['name'] = checkin['venue']['name']
        checkin_dict['id'] = checkin['id']
        checkin_dict['created_at'] = checkin['createdAt']
        #checkin_dict['created_at'] = datetime.datetime.fromtimestamp(checkin['createdAt'])
        categories = checkin['venue']['categories']
        checkin_dict['category'] = categories[0]['name'].lower().encode('utf-8') if len(categories) > 0 else ''
        for category in categories:
            if 'primary' in category and category['primary']:
                checkin_dict['category'] = category['name'].lower()
        checkins.append(checkin_dict)
        if is_invalid_category(checkin_dict['category']):
            blacklisted_checkins.append(checkin_dict)
        else:
            valid_checkins.append(checkin_dict)

for file in json_files:
    with open(file) as f:
        response = json.load(f)
        checkins_json = response['response']['checkins']['items']
        get_checkins(checkins_json)

with open('valid_checkins.txt', 'w') as f:
    json.dump(valid_checkins, f, indent=4)

print 'blacklisted: ' + str(len(blacklisted_checkins)), 'valid: ' + str(len(valid_checkins)), 'total: ' + str(len(checkins))
