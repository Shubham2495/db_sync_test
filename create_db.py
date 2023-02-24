# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:26:00 2023

@author: shubh
"""

from metabase_api import Metabase_API
import pandas as pd
import os
import json
import datetime

import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://crm_user:HTGxvM6McF,3Zb.p@localhost/RDS')


mb = Metabase_API('https://hq-dashboard.nhancebyphoenix.com/', 'shubham@unifynd.com', '123KIngsley!')
print("Fetching users")
users=mb.get_card_data(card_id=2261)
print("users fetched")
users2=pd.DataFrame(users)
print("writing users")
users2.to_sql('customerUser', con=engine)
print("users done")


print("Fetching scans")
scan=mb.get_card_data(card_id=2266)
print("scans fetched")
scan2=pd.DataFrame(scan)
print("writing scans")
scan2.to_sql('customerScans', con=engine)
print("scans done")



print("Fetching coupons")
coup=mb.get_card_data(card_id=2262)
print("coupons fetched")
coup2=pd.DataFrame(coup)
print("writing coups")
coup2.to_sql('couponTransactions', con=engine)
print("coupos done")


print("Fetching rewards")
rewd=mb.get_card_data(card_id=2263)
print("rewards fetched")
rewd2=pd.DataFrame(rewd)
print("writing rewd")
rewd2.to_sql('rewardTransactions', con=engine)
print("rewd done")



print("Fetching scratchCard")
sc=mb.get_card_data(card_id=2264)
print("scratchcards fetched")
sc2=pd.DataFrame(sc)
print("writing sc2")
sc2.to_sql('scratcCardTransactions', con=engine)
print("sc2 done")




print("Fetching spinwheel")
sw=mb.get_card_data(card_id=2265)
print("spinwheel fetched")
sw2=pd.DataFrame(sw)
print("writing sw2")
sw2.to_sql('spinWheelTransactions', con=engine)
print("sw2 done")







