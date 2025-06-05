#%% Zelle 1
import pandas as pd

dataframe= pd.read_csv("../data/activities/activity.csv", sep= ",")
dataframe                  
# %%

dataframe['HeartRate'].min()
dataframe['HeartRate'].max()
dataframe['HeartRate'].mean()
df_statistics = dataframe[['PowerOriginal', 'HeartRate']].describe()
df_statistics.to_markdown

# %%
print(dataframe['PowerOriginal'].mean())
print(dataframe['PowerOriginal'].max())

# %%
dataframe['PowerOriginal'].plot()

# %% Wie lange ist die Leistung über 300W?
dataframe['PowerOriginal'] > 300
dataframe['PeakPower'] = dataframe['PowerOriginal'] > 300

dataframe['PeakPower'].sum()
dataframe['PeakPower'].value_counts()

# %%
dataframe['Zone'] = None

hr_max= dataframe['HeartRate'].max()
hr_max

# %%
untergrenzen_zone = {}
zone= 1
for factor in range (50, 100, 10):
    untergrenzen_zone['Zone ' + str(zone)] = float(hr_max * factor/100)
    zone += 1
untergrenzen_zone

# %%
list_zone= []
for index,row in dataframe.iterrows():
    current_hr = row['HeartRate']
    if current_hr >= untergrenzen_zone['Zone 5']:
        list_zone.append('Zone 5')
    elif current_hr >= untergrenzen_zone['Zone 4']:
        list_zone.append('Zone 4')
    elif current_hr >= untergrenzen_zone['Zone 3']:
        list_zone.append('Zone 3')
    elif current_hr >= untergrenzen_zone['Zone 2']:
        list_zone.append('Zone 2')
    else: 
        list_zone.append('Zone 1')

dataframe['Zone'] = list_zone
dataframe['Zone'].value_counts()

# %%
dataframe_zone_mean = dataframe.groupby('Zone').mean()
dataframe_zone_mean

# %%
import plotly.express as px

fig = px.line(dataframe, y= 'HeartRate')
fig.show()

# %%
import pandas as pd

# Creating a dictionary to store the results
dataframe_mean_power_chart = {}

# Mean power per Zone
dataframe_mean_power_chart['mean_power'] = dataframe.groupby('Zone')['PowerOriginal'].mean()

# Count of entries per Zone (each count equals 1s)
dataframe_mean_power_chart['duration_in_zone'] = dataframe.groupby('Zone').size()

# Converting to a DataFrame for a structured table output
df_result = pd.DataFrame(dataframe_mean_power_chart)

# Filtering for Zones 1-5
df_result = df_result.loc[[1, 2, 3, 4, 5]]

# Displaying the table
print(df_result)

# %%
