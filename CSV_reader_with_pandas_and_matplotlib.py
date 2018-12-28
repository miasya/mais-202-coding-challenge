# Uses Pandas to manage csv data - Final data outputted to shell
# Uses Matplotlib to show a bar graph

import pandas as pd
import matplotlib.pyplot as plt

# Input: Get all data from CSV then remove all but the "purpose" and "int_rate" columns
data_frame = pd.read_csv("data.csv")
data_frame = data_frame[["purpose", "int_rate"]]

# Process data by sorting by purpose and get the average
data_frame = data_frame.groupby("purpose").mean()
data_frame.columns = ["avg_rate"] # Rename from former title int_rate

# Output: Values to shell/console
print(data_frame)

# Output: Bar chart using matplotlib
plot = data_frame.plot.bar(y="avg_rate",rot=90)
plt.ylabel("Average Interest Rate (%)")
plt.xlabel("Purpose")
plt.title("Average Interest Rate By Purpose")
plt.tight_layout()
plt.show()
