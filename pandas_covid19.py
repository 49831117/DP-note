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
twindex = data[condition].index # Taiwan* 的索引值為 240
twdata = np.array(data.iloc[twindex])
twdata = twdata[0][4:] # 此為每日累積確診人數
# column=0~3 ：Province/State, Country/Region, Lat, Long

twdata2 = twdata.copy() # 另存一份，用以紀錄每日新增確診人數
print(twdata)

for i in range(1,len(twdata)):
    twdata2[i] = twdata[i] - twdata[i-1] # 紀錄每日新增確診人數
print(twdata2)
print(data.columns[4:])



import matplotlib.pyplot as plt

index = np.arange(len(twdata)) # 若直接印出日期 X 軸太多文字 #index = data.columns[4:]

# plt.plot(index, twdata) # 累積人數
# plt.xlabel("Date") # X 軸
# plt.ylabel("person") # Y 軸
# plt.title("COVID-19 accumulation confirmed of Taiwan") # 圖表名稱
# plt.show() # 印出圖表

# plt.plot(index, twdata2)
# plt.xlabel("Date")
# plt.ylabel("person")
# plt.title("COVID-19 confirmed of Taiwan")
# plt.show()

plt.plot(index, twdata)
plt.plot(index, twdata2*15) # 每日確診人數的數值放大 20 倍，僅為方便觀察
plt.xlabel("Date")
plt.ylabel("person")
plt.title("COVID-19 confirmed and accumulation confirmed of Taiwan")
plt.show()
