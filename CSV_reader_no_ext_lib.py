# Here is my first solution in Python where I avoided installing any external libraries
# Note I usually use C++ but it was fun to try out Python!
# Looking forward to trying out new library functions to make a prettier solution haha
# Going to experiment with NumPy and Matplotlib as my next step!

import csv
from collections import namedtuple

Pair = namedtuple("Pair", ["first", "second"]) # first is int_rate and second is purpose
pairs = [] # list of pairs to store every int_rate and purpose from csv

# Input data from csv
with open("data.csv", 'r') as csvfile:
    # Use csv.DictReader() so I can refer to items by name instead of position
    reader = csv.DictReader(csvfile)
    for row in reader:
        pairs.append(Pair(row['int_rate'], row['purpose']))
        
csvfile.close()

# Calculating averages and storing in a list where all purposes are unique
pairs.sort(key=lambda x: x[1]) # sort alphabetically by purpose
data = []# list of pairs for avg_rate and purpose
cur_purpose = pairs[0].second
cur_sum = 0.0
num_terms = 0
pairs.append(Pair(0.0, "end")) # Brute force solution to off by one error at end

for pair in pairs:
    if cur_purpose != pair.second:
        avg_rate = float(cur_sum/num_terms)
        data.append(Pair(avg_rate, cur_purpose))
        cur_purpose = pair.second # reset
        cur_sum = float(pair.first) # reset
        num_terms = 1 # reset
    else:
        cur_sum += float(pair.first)
        num_terms += 1
  
# Final output with formatting to resemble a bar chart
print("                    Avg_rate purpose")
for pair in data:
    for x in range(0,int(pair.first)):
        print("*", end = "")
    for x in range(int(pair.first), 20):
        print(" ", end = "")
    print("{:6.3f}" .format(pair.first), " ", pair.second)
