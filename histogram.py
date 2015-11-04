import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv

# example data
mu = 15324  # mean of distribution
sigma = 2973  # standard deviation of distribution
# x = mu + sigma * np.random.randn(10000)

times = []

with open('men18-29_2014.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
    	if(len(row)>12):
    		nums = map(lambda x: int(x), row[12].split(":"))
    		seconds = nums[0] * 3600 + nums[1] * 60 + nums[2]
    		times.append(seconds)

num_bins = 50

# the histogram of the data
n, bins, patches = plt.hist(times, num_bins, normed=1, facecolor='blue', alpha=0.5)
# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Time')
plt.ylabel('Probability')
plt.title(r'2014 Marathon Times - 18-29y/o males')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()