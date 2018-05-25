
import win32com.client
import numpy as np
import matplotlib.pyplot as plt

picoVNACOMObj = win32com.client.Dispatch("PicoControl2.PicoVNA_2")

print("Connecting VNA")
findVNA = picoVNACOMObj.FND()
print('VNA ' + str(findVNA) + ' Loaded')

print("Load Calibration")
ans=picoVNACOMObj.LoadCal('?');
print("Result " + str(ans))

print("Making Measurement")
picoVNACOMObj.Measure('ALL');

print("getting S11 LogMag Data")
raw = picoVNACOMObj.GetData("S11","logmag",0)
splitdata = raw.split(',')
converteddata = np.array(splitdata)
converteddata = converteddata.astype(np.float)
frequency = converteddata[: : 2]
data = converteddata[1 : : 2]

plt.plot(frequency, data)
plt.ylabel("S11 LogMag")
plt.xlabel("Frequency")
plt.show()

a = picoVNACOMObj.CloseVNA()

print("VNA Closed")