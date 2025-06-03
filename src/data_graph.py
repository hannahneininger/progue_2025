# %%

import plotly.express as px
import matplotlib.pyplot as plt
from analyze_activity_data import zone_ranges_df
import pandas as pd 

dataframe = pd.read_csv("./data/activity.csv")
heartrate = dataframe["HeartRate"]
power = dataframe["PowerOriginal"]

fig, ax1 = plt.subplots()

# Erste Y-Achse: Herzfrequenz
color = 'tab:red'
ax1.set_xlabel('Zeit (Index)')
ax1.set_ylabel('Herzfrequenz', color=color)
ax1.plot(heartrate.index, heartrate, color=color, label='Herzfrequenz')
ax1.tick_params(axis='y', labelcolor=color)

# Zonen farblich markieren (basierend auf zone_ranges_df)
for _, row in zone_ranges_df.iterrows():
    ax1.axhspan(row['min'], row['max'], color=row.get('color', 'gray'), alpha=0.2, label=row.get('zone', None))

# Zweite Y-Achse: Power
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Leistung (Power)', color=color)
ax2.plot(power.index, power, color=color, label='Power')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Herzfrequenz und Power im Vergleich (zwei Y-Achsen)')
plt.show()



# %%
