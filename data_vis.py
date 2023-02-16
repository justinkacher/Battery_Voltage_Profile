import pandas as pd
import matplotlib.pyplot as plt


file = "CC_discharge_MP42A01536.xlsx"
file2 = "CC_discharge_MP42A01526.xlsx"

data = pd.read_excel(file)
data2 = pd.read_excel(file2)

# print(data)

ax = data.plot(x = 'Time',y = 'Voltage (V)')
data2.plot(ax = ax, x='Time',y='Voltage (V)')

plt.show()