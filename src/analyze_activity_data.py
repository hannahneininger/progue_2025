# %% z
import pandas as pd

dataframe = pd.read_csv("../data/activity.csv")
dataframe
# %% [markdown]


dataframe["HeartRate"].min()  # Minimum Herzfrequenz
dataframe["HeartRate"].max()  # Maximum Herzfrequenz
dataframe["HeartRate"].mean()  # Durchschnittliche Herzfrequenz
df_statistics = dataframe[["HeartRate","PowerOriginal"]].describe()  # Statistische Kennzahlen
print(df_statistics)


#dataframe.columns


# %%
dataframe["PowerOriginal"].mean()
dataframe["PowerOriginal"].max()

# %%

dataframe["PowerOriginal"].plot()


# %% Wie lange ist die Leistung (PowerOriginal) über 300 Watt trainiert?
dataframe["PowerOriginal"] > 300

dataframe["High Power"] = dataframe["PowerOriginal"] > 300
dataframe["High Power"]

dataframe["High Power"].sum()  # Anzahl der Zeilen, in denen die Bedingung erfüllt ist
dataframe["High Power"].value_counts() # wie oft True und False vorkommen


# %%
dataframe["Zone"] = None

hr_max = dataframe["HeartRate"].max()
hr_max
# %%

untergrenzen_zonen = {} # dictionary für die unterggrenzen der zonen anlegen

zone = 1
for faktor in  range (50,110,10):
    untergrenzen_zonen["Zone " + str(zone)] = float(faktor / 100 * hr_max)
    #print("Zone", zone)
    #print(hr_max * float(faktor/100))
    zone =zone +1 # andere schreibweise zone+= 1

untergrenzen_zonen

# %% Füge eine neue Spalte "Zone" hinzu, die die Zone der Herzfrequenz angibt

list_zone = []  # Liste für die Zonen anlegen




dataframe["Zone"] = None # fügt neue Spalte in das datefraem von "activity.csv" ein 

for index, row in dataframe.iterrows():
    #print(index)
    #print(row["HeartRate"]) # zeigt ersten Wert der Spalte "HeartRate" an
    current_hr = row["HeartRate"]
    
    if current_hr >= untergrenzen_zonen["Zone 5"]:
        list_zone.append("Zone 5")
    elif current_hr >= untergrenzen_zonen["Zone 4"]:
        list_zone.append("Zone 4")
    elif current_hr >= untergrenzen_zonen["Zone 3"]: 
        list_zone.append("Zone 3")
    elif current_hr >= untergrenzen_zonen["Zone 2"]:
        list_zone.append("Zone 2")
    elif current_hr >= untergrenzen_zonen["Zone 1"]:
        list_zone.append("Zone 1")
    else:
        list_zone.append("Zone 0")

    #print(list_zone)

dataframe["Zone"] = list_zone
print(dataframe["Zone"].value_counts()) # summe, wie viel sekunden in der jeweilgen zone verbracht wurden



# %%
dataframe.groupby("Zone").mean()  # alle Zone 1 "in einen Topf", alle TOne 2 in einenm Top als einzelne Zeilen für jede zone

df_groups = dataframe.groupby("Zone").mean()

print(df_groups["HeartRate"])  # Durchschnittliche Herzfrequenz pro Zone



# %%
