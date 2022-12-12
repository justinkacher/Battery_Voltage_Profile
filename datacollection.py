import pandas as pd
import time
import Keithley2450_wrapper.main as keithley    #also initializes connection to keithley


#Make sure to change TCP_IP in main.py to match keithley address
#initialization vars
use_keithley_load = False   #T-uses keithley as current source F-uses external curr load to be set manually
current_load = 2            #in amps
#where the excel dataframe will be saved
path = ""       #no path will save in folder of program  

batteryID = input("scan battery or enter battery ID num: ")
timearr = []
voltagearr = []
curr_loadarr = []
powerarr = []
datadict = {"Time":timearr,"Voltage (V)":voltagearr,"Current Load (A)":curr_loadarr,"Watts (W)":powerarr}
df = pd.DataFrame(data = datadict)
df.to_excel(path+"CC_discharge_"+str(batteryID)+".xlsx")

def savedata():
    df = pd.DataFrame(data = datadict)
    df.to_excel(path+"CC_discharge_"+str(batteryID)+".xlsx")



start_time = time.time()
timearr.append(0)
voltagearr.append(keithley.get_voltage(20))
curr_loadarr.append(current_load)
powerarr.append(0)


if use_keithley_load:
    keithley.current_output_on(current_load)
i = 0
while (voltagearr[i]) > -1:
    voltage = keithley.get_voltage(20)
    timearr.append(time.time()-start_time)
    voltagearr.append(voltage)
    curr_loadarr.append(current_load)
    powerarr.append(voltage*current_load)
    i+=1
    savedata()
    print(datadict)
    time.sleep(5)









