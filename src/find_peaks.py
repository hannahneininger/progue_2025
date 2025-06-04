# %%



import pandas as pd

df = pd.read_csv("../data/ekg_data/01_Ruhe.txt", sep = "	") # seperieren das alle daten eigene spaöte haben

df.columns = ["Voltage in mV", "Time in ms"]
df
# %%

df["is peak"] = None # neue spalte an dataframe hinzufügen

# %%

thershold = 340

df = df.iloc[0:5000]
list_of_peaks = []



for index, row in df.iterrows():
    #print(index)
    #print(row)
    if index == df.index.max(): # wenn index der letzte ist, dann abbrechen, weil sonst indx + 1 nihct funkioniert und es dann crashed
        break

    current_value = row["Voltage in mV"]
    #print("current value: ", current_value)

    #  ist der current value größer als vorgänger und nachfolger
    if current_value > df.iloc[index-1]["Voltage in mV"] and current_value >= df.iloc[index+1]["Voltage in mV"]:
        #print("Found peak at: ", index)
        if current_value > thershold:
            list_of_peaks.append(index) # nur peaks hinzufügen, die über 340 sind 

print(list_of_peaks)
    
# %%

df["is peak"] = False
df.loc[list_of_peaks, "is peak"] = True
df["is peak"].value_counts()

# %% make a plotly plot with the data and highlight the peaks
import plotly.express as px
fig = px.line(df, x="Time in ms", y="Voltage in mV", title="EKG Data with Peaks Highlighted")
fig.add_scatter(x=df[df["is peak"]]["Time in ms"], y=df[df["is peak"]]["Voltage in mV"], mode='markers', name='Peaks', marker=dict(color='red', size=5))
fig.show()

# %%
def find_peaks(df, threshold, ):
    """
    Find peaks in the EKG data based on the given threshold.    
    """
    for index, row in df.iterrows():
        if index == df.index.max(): # wenn index der letzte ist, dann abbrechen, weil sonst indx + 1 nihct funkioniert und es dann crashed
            break

        current_value = row["Voltage in mV"]

        #  ist der current value größer als vorgänger und nachfolger
        if current_value > df.iloc[index-1]["Voltage in mV"] and current_value >= df.iloc[index+1]["Voltage in mV"]:
            
            if current_value > thershold:
                list_of_peaks.append(index) # nur peaks hinzufügen, die über 340 sind 


    list_of_peaks
    return list_of_peaks

#if __name__ == "__main__":
    df = pd.read_csv("../data/ekg_data/01_Ruhe.txt", sep = "	") # seperieren das alle daten eigene spaöte haben
    df.columns = ["Voltage in mV", "Time in ms"]
    df

    list_of_peaks = find_peaks(df, 350)

    df["is peak"] = False
    df.loc[list_of_peaks, "is peak"] = True
    df["is peak"].value_counts()


fig = px.line(df, x="Time in ms", y="Voltage in mV", title="EKG Data with Peaks Highlighted")
fig.add_scatter(x=df[df["is peak"]]["Time in ms"], y=df[df["is peak"]]["Voltage in mV"], mode='markers', name='Peaks', marker=dict(color='red', size=5))
fig.show()

# %%
