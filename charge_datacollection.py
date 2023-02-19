import pandas as pd
import time
import Keithley2450_wrapper as keithley    #also initializes connection to keithley


#Make sure to change TCP_IP in main.py to match keithley address
#initialization vars
use_keithley_load = False   #T: use keithley as current source F: use external curr load to be set manually
current_input = 2            #in amps
v_input = 4.2


#where the excel dataframe will be saved
path = ""       #no path will save in folder of program  

batteryID = input("scan battery or enter battery ID num: ")
timearr = []
voltagearr = []
curr_inp_arr = []
powerarr = []
v_inp_arr = []
datadict = {"Time":timearr,"Voltage (V)":voltagearr,"Current Input (A)":curr_inp_arr,"Voltage Input (V)":v_inp_arr,"Watts (W)":powerarr}
df = pd.DataFrame(data = datadict)
df.to_excel(path+"CC_charge_"+str(batteryID)+".xlsx")

def savedata():
    df = pd.DataFrame(data = datadict)
    df.to_excel(path+"CC_discharge_"+str(batteryID)+".xlsx")



start_time = time.time()
timearr.append(0)
voltagearr.append(keithley.get_voltage(20))
curr_inp_arr.append(current_input)
v_inp_arr.append(v_input)
powerarr.append(0)



#first run was done incorrectly, constant power, battery voltage*2A ~ 7.4W
# note that the charging current was not 2 amps though, the charging voltage was constant at 4.2V

if use_keithley_load:
    keithley.current_output_on(current_input)
i = 0
while (voltagearr[i]) < 4.25:
    voltage = keithley.get_voltage(20)
    timearr.append(time.time()-start_time)
    voltagearr.append(voltage)
    curr_inp_arr.append(current_input)
    v_inp_arr.append(v_input)
    powerarr.append(voltage*current_input)
    i+=1
    savedata()
    print(datadict)
    time.sleep(5)

print("\n\n\ntest complete")









