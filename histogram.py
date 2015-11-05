import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy
import scipy.stats as stats
from scipy.stats import normaltest
from scipy.stats import mstats
import csv
import math
import sys
import glob
import argparse

parser = argparse.ArgumentParser(description='Create a histogram.')

parser.add_argument('--dir', default="data",
                   help='select a directory of csv files')

args = parser.parse_args()

times = []
files = glob.glob("{0}/*.csv".format(args.dir))

for phile in files:
	with open(phile, 'rb') as csvfile:
	    reader = csv.reader(csvfile, delimiter=',')
	    for row in reader:
	    	if(len(row)>12):
	    		nums = map(lambda x: int(x), row[12].split(":"))
	    		seconds = nums[0] * 3600 + nums[1] * 60 + nums[2]
	    		times.append(seconds)

print(normaltest(times))
print(mstats.skewtest(times))
print(stats.describe(times))

n, (smin, smax), sm, sv, ss, sk = stats.describe(times)
num_bins = 50

# the histogram of the data
n, bins, patches = plt.hist(times, num_bins, normed=1, facecolor='blue', alpha=0.5)

# add a 'best fit' line
y = mlab.normpdf(bins, sm, math.sqrt(sv))
plt.plot(bins, y, 'r--')
plt.xlabel('Time')
plt.ylabel('Probability')
plt.title(r'2014 NYC Marathon Times')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()