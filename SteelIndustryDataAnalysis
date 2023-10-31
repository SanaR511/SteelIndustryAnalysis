import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

industry = pd.read_csv(r'C:\Users\Sana R\Downloads\SteelIndustry.csv')
industry.head()

industry['Leading_Current_Power_Factor'].min()

industry['Leading_Current_Power_Factor'].value_counts()

#Freq table of load
loads = industry["Load_Type"].value_counts()
print(loads)

loadType = ["Light Load","Maximum Load","Medium Load"]
availability = [18072, 9696, 7272]
plt.bar(loadType, availability, color=("blue","orange", "green"))
plt.xlabel("Load Type")
plt.ylabel("Frequency")
plt.title("     Figure 1: Total Frequency vs Load Type")
plt.show()

#Freq table of WeekStatus
weekStatus = industry["WeekStatus"].value_counts()
print(weekStatus)

loadType = ["Weekday","Weekend"]
availability = [25056, 9984]
plt.bar(loadType, availability, color=("purple","hotpink"))
plt.xlabel("Week Status")
plt.ylabel("Frequency")
plt.title("     Figure 2: Total Frequency vs Week Status")
plt.show()


#scatter plot usage kWh vs CO2
sns.lmplot(x="CO2(tCO2)", y="Usage_kWh", data=industry).set(title='Figure 4: Energy Usage by CO2 ')

#Checking for any null data
industry.isnull().sum()

#Binning

df_industry = pd.DataFrame(industry, columns=['Lagging_Current_Reactive.Power_kVarh', 'Leading_Current_Reactive_Power_kVarh', 'CO2(tCO2)', 'Lagging_Current_Power_Factor','Leading_Current_Power_Factor'])                                     
df_industry

#Cutting
df_industry['Leading_Current_Power_Factor bins'] = pd.cut(df_industry['Leading_Current_Power_Factor'], 10)
df_industry
