from csv import reader
import numpy as np
from math import *

with open('FRED.csv', 'r') as read_obj:

    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)

data = []

for index in range(len(list_of_rows)):

    data.append(float(list_of_rows[index][0]))

print(data)

data.reverse()
# Find the exponentially-weighted mean

alpha = 0.5
mean = data[9]
count = 2
threshold = 7

# Fit an exponential line to the data points

# Calculate variance using delta(abs(real - fitted))

# calculate the next month's data point


index = 8
while (index >= 0):

    mean = alpha*data[index] + (1-alpha)*mean
    index -= 1

print(mean)

variance = np.var(data[0:9])

print(variance)

cdf = (1.0 + erf((threshold-mean) / sqrt(2.0*variance))) / 2.0

print(cdf)


# Find the variance (exponentially-weight)


