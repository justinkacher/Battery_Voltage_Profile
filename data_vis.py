import pandas as pd
import matplotlib.pyplot as plt


file = "CC_discharge_MP42A01526.xlsx"

data = pd.read_excel(file)

# print(data)

data.plot(x = 'Time',y = 'Voltage (V)')
plt.show()