import math

from user_data.score.composite_score import haggle
from user_data.score.composite_score import get_acceptance_probability
from config import NEXT_ZONE_ACCEPTANCE, LAST_ZONE_ACCEPTANCE

def should_return_bid():
    scores = [0.685360179796, 0.346430539388, 0.659653036939,
              0.669001247, 0.560706768404, 0.756308799865,
              0.801327511515, 0.708212147755, 0.684039746209,
              0.765256073878, 0.703803036939, 0.576090929301,
              0.80377643347, 0.685571474236, 0.741082165689,
              0.699022021564, 0.488709804534, 0.650929429575]
    success = 0
    failure = 0
    for score in scores:
        for i in range(100):
            counter_offer = haggle(35.0, score, 5.0, 35.0, 10, 10)
            if counter_offer == 35.0:
                success += 1
            else:
                failure += 1
    print success, " ", failure
    i = 1 / 0
