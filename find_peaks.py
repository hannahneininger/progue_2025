# %%
# make a plot with ploty with peaks highlighted
import pandas as pd
import plotly.express as px 


# %%
def find_peaks(df, threshold):
    threshold= 340

    df = df.iloc[0:5000]

    for index, row in df.iterrows():

    #Sorgt dafür, ass wir am Ende keine Problem haben (index+1) ist länger
        if index==df.index.max():
            break


    current_value = row["Voltage in mV"]

    # ist der current_value grösser als vorgänger und nachfolger?
    if current_value > df.iloc[index - 1]["Voltage in mV"] and current_value >= df.iloc[index + 1]["Voltage in mV"]:
        # print("Found Peak at:", index)

        if current_value > threshold:
                list_of_peaks.append(index)


    return list_of_peaks
df = pd.read_csv("data/ekg_data/01_Ruhe.txt" , sep= "	")
df.columns =["Voltage in mV","Time in ms"]
list_of_peaks = []
df["is_peak"] = None



df["is_peak"] = False


threshold= 340
list_of_peaks = []
df = df.iloc[0:5000]

for index, row in df.iterrows():

   #Sorgt dafür, ass wir am Ende keine Problem haben (index+1) ist länger
    if index==df.index.max():
        break

    current_value = row["Voltage in mV"]
    print("current value:", current_value)

    # ist der current_value grösser als vorgänger und nachfolger?
    if current_value > df.iloc[index - 1]["Voltage in mV"] and current_value >= df.iloc[index + 1]["Voltage in mV"]:
       #print("Found Peak at:", index)
       if current_value > threshold:
            list_of_peaks.append(index)
df.loc[list_of_peaks,"is_peak"] = True
df["is_peak"].value_counts()

# %%

fig = px.line(df, x="Time in ms", y="Voltage in mV", title="EKG Data with Peaks")
fig.add_scatter(x=df.loc[df["is_peak"], "Time in ms"], y=df.loc[df["is_peak"], "Voltage in mV"],
                mode='markers', marker=dict(color='red', size=8), name='Peaks')
fig.show()
    
# %%
