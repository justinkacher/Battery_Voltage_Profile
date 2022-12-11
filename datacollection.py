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
    with pd.ExcelWriter(path+"CC_discharge_"+str(batteryID)+".xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
        df.to_excel(writer, sheet_name="Sheet1",header=None, startrow=writer.sheets["Sheet1"].max_row,index=False)



start_time = time.time()



if use_keithley_load:
    keithley.current_output_on(current_load)
i = 0
while voltage[i-1] > 2:
    timearr.append(time.time()-start_time)
    voltagearr.append(keithley.get_voltage(20))
    curr_loadarr.append(current_load)
    i+=1
    savedata()
    time.sleep(5)









