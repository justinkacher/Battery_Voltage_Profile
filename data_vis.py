import pandas as pd
import matplotlib.pyplot as plt
import sympy as sy


file = "CC_discharge_MP42A01536.csv"
file2 = "CC_discharge_MP42A01526.csv"

data = pd.read_csv(file)
data2 = pd.read_csv(file2)


def integrate(dataframe):
    # uses trapezoidal approximation
    time_arr = dataframe['Time']
    volt_arr = dataframe['Voltage (V)']
    sum = 0
    for i in range(0,len(dataframe)):
        try:
            deltat = time_arr[i]-time_arr[i-1]
            h1 = volt_arr[i]
            h2 = volt_arr[i-1]
        except:
            deltat = time_arr[i]-time_arr[i]
            h1 = volt_arr[i]
            h2 = volt_arr[i]

        dx = .5*(h1+h2)*deltat
        sum += dx

    return sum  


print(integrate(data))
print(integrate(data2))
# ax = data.plot(x = 'Time',y = 'Voltage (V)')
# data2.plot(ax = ax, x='Time',y='Voltage (V)')


# plt.show()