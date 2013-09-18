'''
import sys

sys.path.append('../')

import setup 

setup.connect_to('test1')

from model.user import User
from model.oauth2 import Client, Token

user = User.get_or_insert('user1@test.com')
client = Client.new(user, 'client_user1', '/')
token = Token.get_or_create(user, client)
'''

from datetime import datetime
import urllib, urllib2

token = '1c280f3cc3b04f10844c1f760967be54'

url = 'http://haggle-dev.appspot.com/test'
data = { 'token': token} #.id }
request = urllib2.Request(url, urllib.urlencode(data))

error = True 
start_time = datetime.now()

while True:
    line = str(datetime.now())
    try:
        response = urllib2.urlopen(request)
    except urllib2.URLError, e:
        error = True
        error_time = datetime.now()
        print response.info()
        #print (('RateLimit-ResetTime', response.info().getheader('RateLimit-ResetTime')))
        continue
    if error:
        error = False
        #print datetime.now() - start_time 
    line = line + ': ' + 'RateLimit-Remaining ' + response.info().getheader('RateLimit-Remaining')
    print line

