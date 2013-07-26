import sys

sys.path.append('../')

from setup import setup

setup()

from negotiation_engine.deal import Deal, DealStatus
from model.user import User
from model.vendor import Vendor
from model.campaign import Campaign
from util import clock

from datetime import datetime

format = '%m/%d/%y'

vendor = Vendor.get_by_id(166069)
campaign = Campaign.for_(vendor)

deals = Deal.all().filter('campaign', campaign).filter('status =', 4).order('last_updated')

transactions = {}

for deal in deals:
    datetime_object = clock.eastern_datetime(deal._redemption_datetime)
    date = datetime.strftime(datetime_object, format)
    if date in transactions:
        transactions[date] += 1
    else:
        transactions[date] = 1

print transactions

