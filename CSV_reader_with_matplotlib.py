# Uses Matplotlib to show a bar graph
# Note that the average rates per purpose are outputted to the shell to 3 decimal places

import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple

Pair = namedtuple("Pair", ["first", "second"]) # first is int_rate and second is purpose
pairs = [] # list of pairs to store every int_rate and purpose from csv

# Input data from csv
with open("data.csv", 'r') as csvfile:
    # Use csv.DictReader() so I can refer to items by name instead of position
    reader = csv.DictReader(csvfile)
    for row in reader:
        pairs.append(Pair(row["int_rate"], row["purpose"]))
        
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
  
# Output values to shell
for pair in data:
    print("{:6.3f}" .format(pair.first), " ", pair.second)

# Final output with formatting to resemble a bar chart
# Note, I could skip the pairing of the avg_rate and the purpose,
# But I kept it in case we wanted to manipulate the data in a new way later
objects = []
rates = []
for pair in data:
    objects.append(pair.second)
    rates.append(float(pair.first))
#Plotting stuff
y_pos = np.arange(len(objects))
plt.bar(y_pos, rates, align="center")
# Colours :D
colors = ['#deb7ff', '#c785ec', '#a86add', '#8549a7', '#634087']
barlist=plt.bar(objects,rates)
for x in range(0, len(objects)):
    barlist[x].set_color(colors[x%4])
# More plotting stuff
plt.xticks(y_pos, objects, fontsize = 6, rotation = 90)
plt.ylabel("Average Interest Rate (%)")
plt.xlabel("Purpose")
plt.title("Average Interest Rate By Purpose")
plt.tight_layout()
plt.show()


