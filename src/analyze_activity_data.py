# %% z
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

dataframe = pd.read_csv("data/activity.csv")
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
# Erstelle eine Tabelle mit Zone, Minimum und Maximum der Herzfrequenz für jede Zone
zone_ranges = []
for i in range(1, 6):
    zone_name = f"Zone {i}"
    min = untergrenzen_zonen[zone_name]
    if i < 5:
        max_hr = untergrenzen_zonen[f"Zone {i+1}"] - 1
    else:
        max_hr = hr_max
    zone_ranges.append({"Zone": zone_name, "min": min, "max": max_hr})


zone_ranges_df = pd.DataFrame(zone_ranges)
zone_ranges_df
print(zone_ranges_df)



# %%
dataframe.groupby("Zone").mean()  # alle Zone 1 "in einen Topf", alle TOne 2 in einenm Top als einzelne Zeilen für jede zone

df_groups = dataframe.groupby("Zone").mean()

print(df_groups["HeartRate"])  # Durchschnittliche Herzfrequenz pro Zone



# %%

import plotly.express as px

fig = px.line(dataframe, y = "HeartRate")
fig.show()



# %%

dataframe.groupby("Zone").mean()

df_groups_poweroriginal = dataframe.groupby("Zone").mean()["PowerOriginal"]

print(df_groups_poweroriginal)  # Durchschnittliche Leistung pro Zone

#dataframe["PowerOriginal"].value_counts("Zone")  # wie oft welche Leistung vorkommt

#print(dataframe.groupby("Zone").value_counts(["PowerOriginal"]))  # wie oft welche Leistung in welcher Zone vorkommt

#PowerOriginal_in_zones = dataframe.groupby("Zone").value_counts(["PowerOriginal"])

#print(sum(PowerOriginal_in_zones["Zone"]))  # Summe der Werte in PowerOriginal_in_zones
# %%

dataframe.groupby("Zone").mean()  # alle Zone 1 "in einen Topf", alle TOne 2 in einenm Top als einzelne Zeilen für jede zone

df_groups_time = dataframe.groupby("Zone").sum()
df_groups_time_sec = df_groups_time/60  # Umwandlung von Sekunden in Minuten

print(df_groups_time_sec["Duration"])  # Summe der Dauer pro Zone
#print(df_groups["Duration"]) 

# %%


dfresult = pd.DataFrame({"Zone": list(df_groups_time_sec.index), 
                          "Duration" : df_groups_time_sec["Duration"], 
                          "PowerOriginal": df_groups_poweroriginal  
                          })

# entferne die Spalte "Zone"
dfresult = dfresult.reset_index(drop=True)

print(dfresult)


# %%
import pandas as pd
def create_table():
    dataframe = pd.read_csv("data/activity.csv")

    # Berechnung der Zonen
    dataframe["Zone"] = None
    untergrenzen_zonen = {} # dictionary für die unterggrenzen der zonen anlegen

    hr_max = dataframe["HeartRate"].max()
    zone = 1

    for faktor in  range (50,110,10):
        untergrenzen_zonen["Zone " + str(zone)] = float(faktor / 100 * hr_max)
        zone =zone +1 # andere schreibweise zone+= 1


        list_zone = []  # Liste für die Zonen anlegen

    dataframe["Zone"] = None # fügt neue Spalte in das datefraem von "activity.csv" ein 

    for index, row in dataframe.iterrows():
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

    dataframe["Zone"] = list_zone


    dataframe.groupby("Zone").mean()
    df_groups_poweroriginal = dataframe.groupby("Zone").mean()["PowerOriginal"]

    dataframe.groupby("Zone").mean()  # alle Zone 1 "in einen Topf", alle TOne 2 in einenm Top als einzelne Zeilen für jede zone
    df_groups_time = dataframe.groupby("Zone").sum()
    df_groups_time_sec = df_groups_time/60  # Umwandlung von Sekunden in Minuten
    result_time = df_groups_time_sec["Duration"]

    dfresult = pd.DataFrame({"Zone": list(df_groups_time_sec.index), 
                          "Duration" : result_time, 
                          "PowerOriginal": df_groups_poweroriginal  
                          })

    # entferne die Spalte "Zone"
    dfresult = dfresult.reset_index(drop=True)
    return dfresult

dfresult = create_table()  # Aufruf der Funktion create_table


print(dfresult)




# %%
import plotly.graph_objs as go

heartrate = dataframe["HeartRate"]
power = dataframe["PowerOriginal"]

fig = go.Figure()

# Herzfrequenz-Linie
fig.add_trace(go.Scatter(
    x=heartrate.index/60,
    y=heartrate,
    name='Herzfrequenz',
    yaxis='y1',
    line=dict(color='red')
))

# Power-Linie
fig.add_trace(go.Scatter(
    x=power.index/60,
    y=power,
    name='Leistung',
    yaxis='y2',
    line=dict(color='green')
))

# Zonen farblich markieren (als Shapes)
# Einfache Rotabstufungen für die Herzfrequenz-Zonen
zone_colors = ['#ffcccc', '#ff9999', '#ff6666', '#ff3333', '#cc0000']

for i, (_, row) in enumerate(zone_ranges_df.iterrows()):
    fig.add_shape(
        type="rect",
        xref="paper", yref="y1",
        x0=0, x1=1,
        y0=row['min'], y1=row['max'],
        fillcolor=zone_colors[i % len(zone_colors)],
        opacity=0.15,
        layer="below",
        line_width=0,
    )

# Layout mit zwei Y-Achsen und Zoom/Interaktivität
fig.update_layout(
    title="Herzfrequenz & Leistung",
    xaxis=dict(title="Zeit (min)"),
    yaxis=dict(title="Herzfrequenz (bpm)", color='red'),
    yaxis2=dict(title="Leistung (Watt)", overlaying='y', side='right', color='green'),
    legend=dict(x=0.01, y=0.99),
    hovermode='x unified',
)

# Interaktive Zoomfunktion ist standardmäßig in Plotly enthalten (per Drag & Zoom)
fig.write_html("figures/heart_rate_power_curve_interactive.html")
fig.show()





# %%

#power_mean = dataframe["PowerOriginal"].mean()
#power_max = dataframe["PowerOriginal"].max()

# Tabelle mit Mittelwert und Maximalwert der Leistung pro Zone
def power_stats_per_zone():
    return dataframe.groupby("Zone")["PowerOriginal"].agg(Mittelwert="mean", Maximalwert="max")
print(power_stats_per_zone)



# %%
