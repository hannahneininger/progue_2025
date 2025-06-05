# %%

import pandas as pd

df= pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="	")
df.columns = ["Voltage in mV", "Time in ms"]
df

# %%
df["is_peak"] = None
df

# %%
df= df.iloc[0:5000]
list_of_peaks= []
threshold= 340
for index, row in df.iterrows():

    if index == df.index.max():
        break

    current_value= row["Voltage in mV"]
    print("current value: ", current_value)

    #ist current_value größer als vorgänger und nachfolger
    if current_value > df.iloc[index - 1]["Voltage in mV"] and current_value >= df.iloc[index + 1]["Voltage in mV"]:
        print("Found peak at: ", index)

        if current_value >= threshold:
            list_of_peaks.append(index)

print(list_of_peaks)

# %%
df["is_peak"]= False
df.loc[list_of_peaks, "is_peak"] = True
df["is_peak"].value_counts()

# %%
import plotly.express as px

fig= px.line(df, x= "Time in ms", y="Voltage in mV", title= "EKG Data with Peaks")
fig.add_scatter(x= df[df["is_peak"]]["Time in ms"], y= df[df["is_peak"]]["Voltage in mV"], mode= "markers", name= "Peaks", marker= dict(color="red", size=5))
fig.show()
# %%
def find_peaks(df, threshold):
    list_of_peaks= []
    threshold= 340
    for index, row in df.iterrows():
        #Vermeiden, dass am Ende ins nichts iteriert wird:
        if index == df.index.max():
            break

        current_value= row["Voltage in mV"]
        #ist current_value größer als vorgänger und nachfolger
        if current_value > df.iloc[index - 1]["Voltage in mV"] and current_value >= df.iloc[index + 1]["Voltage in mV"]:
        # threshold für peaks
            if current_value >= threshold:
                list_of_peaks.append(index)

    return list_of_peaks
# %%
#überprüfen
df= pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="	")
df.columns = ["Voltage in mV", "Time in ms"]
df

list_of_peaks= find_peaks(df, 340)

df["is_peak"]= False
df.loc[list_of_peaks, "is_peak"] = True
df["is_peak"].value_counts()

fig= px.line(df, x= "Time in ms", y="Voltage in mV", title= "EKG Data with Peaks")
fig.add_scatter(x= df[df["is_peak"]]["Time in ms"], y= df[df["is_peak"]]["Voltage in mV"], mode= "markers", name= "Peaks", marker= dict(color="red", size=5))
fig.show()

# %%
