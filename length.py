# import matplotlib.pyplot as plt
# import pandas as pd

# User_data = pd.read_csv('data.csv')
# duration = User_data['duration_ms']

# musicClip = 0 #10 seconds or less
# minuteMusic = 0 # 10 seconds - 
# twoMinuteMusic = 0
# threeMinuteMusic = 0 
# fourMusic = 0 
# fiveMusic = 0
# aboveFive = 0 
# for item in duration:
#     if item <= 10000: #less than 10 seconds
#         musicClip += 1 
#     if  10000 < item <= 60000:
#         minuteMusic += 1
#     if 60000 < item <= 120000:
#         twoMinuteMusic += 1 
#     if 120000 < item <= 180000:
#         threeMinuteMusic += 1 
#     if 180000 < item <= 240000:
#         fourMusic += 1
#     if 240000 < item <= 300000:
#         fiveMusic += 1
#     if item > 300000:
#         aboveFive += 1

# lengthMusic = []
# howMany = [musicClip, minuteMusic, twoMinuteMusic, threeMinuteMusic, fourMusic, fiveMusic, aboveFive]
# i = " "
# for item in howMany:
#     i += 'I'
#     lengthMusic.append(i)

# greatest = 0
# location = -1
# for item in howMany:
#     if item > greatest:
#         greatest = item
#         location += 1 
#     else:
#         continue

# print("the interval of time that most of your music falls into is: " + str(lengthMusic[location]))

# plt.bar(lengthMusic, howMany)
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd

duration = pd.read_csv('data.csv')['duration_ms'].to_list()
duration.sort()

def count_range_in_list(arr, min, max=None):
	ctr = 0
	for x in arr:
		if max != None:
			if min <= x <= max:
				ctr += 1
		else:
			if min <= x:
				ctr += 1
	return ctr

items = {}
times = [0, 10000, 60000, 120000, 180000, 240000, 300000, None]
for i in range(len(times) - 1):
	items[i + 1] = count_range_in_list(duration, times[i], times[i+1])

print("the interval of time that most of your music falls into is: " + str(list(items.keys())[list(items.values()).index(max(items.values()))]))
x, y = zip(*sorted(items.items()))
plt.bar(x, y)
plt.show()