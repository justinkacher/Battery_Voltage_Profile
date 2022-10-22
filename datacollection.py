from locale import currency
from re import I
import pandas as pd
import time
import Keithley2450_wrapper.main as keithley

curr_load = input("current load: ")
batteryID = input("scan battery or enter battery ID num: ")

start_time = time.time
keithley.current_output_on(curr_load)
i=0
while voltage[i-1] > 1:
    timearr[i] = time.time-start_time
    voltagearr[i] = keithley.get_voltage(20)
    real_currarr[i] = keithley.get_current(1.05)
    powerarr[i] = voltagearr[i]*real_curr[i]
    curr_loadarr[i] = curr_load
    i+=1
    time.sleep(10)

dict = {"Time":timearr,"Voltage (V)":voltagearr,"Current Load (A)":curr_loadarr,"Real Current (A)":real_currarr,"Watts (W)":powerarr}
df = pd.DataFrame(data = dict)
df.to_excel(str(batteryID))



