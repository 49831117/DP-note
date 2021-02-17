import pandas as pd
import numpy as np
#收集資料 https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases

#讀取資料
data = pd.read_csv("time_series_covid19_confirmed_global.csv")

#觀察資料
# print("資料數量", data.shape) # 幾欄、幾列
# print("資料欄位", data.columns) 
# print(data["Country/Region"][240])


condition = data["Country/Region"] == "Taiwan*" # 布林值
twindex = data[condition].index
twdata = np.array(data.iloc[twindex])
twdata = twdata[0][4:]
twdata2 = twdata.copy()
print(twdata)

for i in range(1,len(twdata)):
    twdata2[i] = twdata[i] - twdata[i-1]
print(twdata2)
print(data.columns[4:])


# import matplotlib.pyplot as plt
# index = np.arange(len(twdata))
# #index = data.columns[4:]
# plt.plot(index, twdata)
# plt.xlabel("Date")
# plt.ylabel("person")
# plt.title("COVID-19 accumulation confirmed of Taiwan")
# plt.show()

# twdata2=twdata.copy()
# twdata2[0]=twdata[0] #twdata2:台灣每日確診人數
# for i in range(1,len(twdata)):    
#     twdata2[i]=twdata[i]-twdata[i-1]
# plt.plot(index, twdata2)
# plt.xlabel("Date")
# plt.ylabel("person")
# plt.title("COVID-19 confirmed of Taiwan")
# plt.show()

# twdata2=twdata.copy()
# twdata2[0]=twdata[0] #twdata2:台灣每日確診人數
# for i in range(1,len(twdata)):    
#     twdata2[i]=twdata[i]-twdata[i-1]
# plt.plot(index, twdata)
# plt.plot(index, twdata2*20)
# plt.xlabel("Date")
# plt.ylabel("person")
# plt.title("COVID-19 confirmed and accumulation confirmed of Taiwan")
# plt.show()
