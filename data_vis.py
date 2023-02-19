import pandas as pd
import matplotlib.pyplot as plt
import sympy as sy


file = "CC_discharge_MP42A01536.csv"
file2 = "CC_discharge_MP42A01526.csv"




data = pd.read_csv(file)
data2 = pd.read_csv(file2)




AH = []
def integrate(dataframe):
    # uses trapezoidal approximation
    time_arr = dataframe['Time']
    volt_arr = dataframe['Voltage (V)']
    sum = 0

    # convert time to amp hours
    AH = []
    AH_sum = [0]

    for i in range(0,len(dataframe)):
        try:
            deltat = time_arr[i]-time_arr[i-1]
            h1 = volt_arr[i]
            h2 = volt_arr[i-1]
        except:
            deltat = time_arr[i]-time_arr[i]
            h1 = volt_arr[i]
            h2 = volt_arr[i]


        # this should be *2 amps, yeilds half battery capacity though? *4 matches datasheet
        AH.append((deltat/(60*60))*4)
        AH_sum.append(AH[i] + AH_sum[i-1])
        
        dx = .5*(h1+h2)*AH[i]
        sum += dx
    
    

    volt = data['Voltage (V)']
    AH_sum.pop(0)
    chartdict = {'volt':dataframe['Voltage (V)'],'amp hours':AH_sum}
    newdf = pd.DataFrame(chartdict)



    return newdf,sum




#single cell stats
print("individual cell characteristic")
newdf1,pwr1 = integrate(data)
newdf2,pwr2 = integrate(data2)

print("Power @ 4.2V: ",pwr1," Watts")
print("Power @ 4.0V: ",pwr2," Watts")
ax = newdf1.plot(x = 'amp hours',y = 'volt')
newdf2.plot(ax = ax,x = 'amp hours',y = 'volt',title='Single Cell Characteristic')
plt.show()



def total_power(df):
    amparr = df['amp hours'] 
    voltarr = df['volt']
    sum = 0
    for i in range(0,len(df)):
        try:
            deltaamp = amparr[i]-amparr[i-1]
            h1 = voltarr[i]
            h2 = voltarr[i-1]
        except:
            deltaamp = amparr[i]-amparr[i]
            h1 = voltarr[i]
            h2 = voltarr[i]
        dx = .5*(h1+h2)*deltaamp
        sum += dx

    return sum



#whole pack stats

# 4V 104 series of 13 parallels
# Amp Hours * 13
# voltage * 104

for i in range(0,(len(newdf2['volt']))):
    (newdf2['volt'])[i] = ((newdf2['volt'])[i]*104)
for i in range(0,(len(newdf2['amp hours']))):
    (newdf2['amp hours'])[i] = ((newdf2['amp hours'])[i])*13
# print(newdf2)
print("total power @ 4.0v",total_power(newdf2)," Watts")


# 4.2V 100 series of 13 parallels
# Amp Hours *13
# voltage * 100

for i in range(0,(len(newdf1['volt']))):
    (newdf1['volt'])[i] = ((newdf1['volt'])[i]*100)
for i in range(0,(len(newdf1['amp hours']))):
    (newdf1['amp hours'])[i] = ((newdf1['amp hours'])[i])*13
# print(newdf1)
print("total power @ 4.2V",total_power(newdf1)," Watts")

#red is df1, 4.2v charge
#blue is df2, 4.0V charge
ax = newdf1.plot(x = 'amp hours',y = 'volt',color = 'red')
newdf2.plot(ax = ax,x = 'amp hours',y = 'volt',title="Full Pack Characteristic")
plt.show()

