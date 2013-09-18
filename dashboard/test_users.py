import sys

sys.path.append('../')

from setup import setup

setup.connect_to('test1')

from negotiation_engine.deal import Deal, DealStatus
from model.user import User
from model.vendor import Vendor
from model.campaign import Campaign
from util import clock

from datetime import datetime

format = '%m/%d/%y'

vendor = Vendor.get_by_id(166069)
campaign = Campaign.for_(vendor)

deals = Deal.all().filter('campaign', campaign).filter('status =', 4).order('_redemption_datetime')

old_users = []
new_users = {}

for deal in deals:
    datetime_object = clock.eastern_datetime(deal._redemption_datetime)
    date = datetime.strftime(datetime_object, format)
    user = deal.user
    if not user.name in old_users:
        if date in new_users: 
            new_users[date] += 1
        else:
            new_users[date] = 1
        old_users.append(user.name)

print new_users
