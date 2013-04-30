import json

with open('valid_checkins.txt') as f:
    checkins_fs = json.load(f)

f = open('checkins_test1')

ids_test1 = [] 
ids_fs = []
checkins_test1 = []

for line in f.readlines():
    checkins_dict = {}
    user = line.split(',')[4]
    network = line.split(',')[1]
    if user == 'resnick.matthew@gmail.com' and network == '4S':
        checkins_dict['id'] = line.split(',')[3]
        checkins_dict['vendor_id'] = line.split(',')[0]
        checkins_test1.append(checkins_dict)
        ids_test1.append(line.split(',')[3])

for checkin in checkins_fs:
    ids_fs.append(checkin['id'])

print 'checkins in db: ' + str(len(checkins_test1)), 'checkins in json: ' + str(len(checkins_fs))

print '\ncheckins from json not in db'
for checkin in checkins_fs:
    if not checkin['id'] in ids_test1:
        print checkin 

print '\ncheckins from db not in json'
for checkin in checkins_test1:
    if not checkin['id'] in ids_fs:
        print checkin
