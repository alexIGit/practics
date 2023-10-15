from datetime import datetime
from dateutil.parser import parse

# import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns
# import statsmodels as sm

# now = datetime.now()
# print('now', now, sep=': ') 
# print(now.year, now.month, now.day)

# delta= datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
# print('timedelta: ', delta)
# print('delta.days: ', delta.days)

# parse_date= parse('2011-01-03')
# print(parse_date)


datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
# pd_date = pd.to_datetime(datestrs)
# print(pd_date)

idx = pd.to_datetime(datestrs + [None])
print(idx)