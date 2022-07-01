import csv
from pickletools import int4
import string

# seed the pseudorandom number generator
from random import seed
from random import random
from xmlrpc.client import DateTime
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
from datetime import timedelta
import pandas as pd
from matplotlib import dates as mpl_dates
from datetime import datetime
import numpy
import random
import sys
import datetime

import seaborn as sns
User_data = pd.read_csv('/Users/matthewzhang/Desktop/Data/data.csv')
duration = User_data['duration_ms']

musicClip = 0 #10 seconds or less
minuteMusic = 0 # 10 seconds - 
twoMinuteMusic = 0
threeMinuteMusic = 0 
fourMusic = 0 
fiveMusic = 0
aboveFive = 0 
for item in duration:
    if item <= 10000: #less than 10 seconds
        musicClip += 1 
    if  10000 < item <= 60000:
        minuteMusic += 1
    if 60000 < item <= 120000:
        twoMinuteMusic += 1 
    if 120000 < item <= 180000:
        threeMinuteMusic += 1 
    if 180000 < item <= 240000:
        fourMusic += 1
    if 240000 < item <= 300000:
        fiveMusic += 1
    if item > 300000:
        aboveFive += 1

lengthMusic = []
howMany = [musicClip, minuteMusic, twoMinuteMusic, threeMinuteMusic, fourMusic, fiveMusic, aboveFive]
i = " "
for item in howMany:
    i += 'I'
    lengthMusic.append(i)

greatest = 0
location = -1
for item in howMany:
    if item > greatest:
        greatest = item
        location += 1 
    else:
        continue

    
print("the interval of time that most of your music falls into is: " + str(lengthMusic[location]))


plt.bar(lengthMusic, howMany)
plt.show()