
# %%
from load_data import load_data
from sort import bubble_sort
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Load the data from the CSV file
    data = load_data('../data/activity.csv')
    power_W = data['PowerOriginal']
    print(power_W)
    sorted_power_W = bubble_sort(power_W)
    print(sorted_power_W[::-1])
    
    fig, ax = plt.subplots()
    a = np.arange(len(sorted_power_W))  
    x = a/60    # Assuming time is the index of the power data
    y = sorted_power_W[::-1] # Use the sorted power data for plotting

    ax.plot(x, y, color='blue')  # Add a line plot for better visualization
    ax.set(xlabel='Time (min)', ylabel='Power (W)',
           title='Power Curve')
    ax.grid()
    plt.show()
    # Save the plot as a PNG file
    fig.savefig("../figures/power_curve.png")

# %%
## VERSUCH 1 von mir

    # Create a DataFrame from the power_W array
# df_Leistungskurve = pd.DataFrame({'Power': power_W})
#     # Sort the DataFrame in descending order by 'Power'
# df_Leistungskurve = df_Leistungskurve.sort_values(by='Power', ascending=False).reset_index(drop=True)
#     # Calculate the maximum time  (Gesamtzeit)
# max_time = len(df_Leistungskurve) / 60  # Assuming each entry represents one second
# print(f"Max time in minutes: {max_time}")
#     # Calculate max time per power value (generalized)
# df_Leistungskurve['Time (min)'] = np.arange(len(df_Leistungskurve)) / 60

# #create new column in df:leistungskurve with sum time consecutive power values
# df_Leistungskurve['Cumulative Time (min)'] = df_Leistungskurve['Time (min)'].cumsum()
# df_Leistungskurve



# %%
##Versuch 2 mit Julian


import pandas as pd
data = load_data('../data/activity.csv')
df = pd.DataFrame(data)
df

power_W = df['PowerOriginal']
power_W

unique_power_values = power_W.unique()
unique_power_values = sorted(unique_power_values, reverse=True)  # Sort in descending order

unique_power_values


# %%

results_dict = {}
# für jeden unique power value
for current_threshold in unique_power_values:
       # gehe durch die power_W und schauen, wenn der überschritten 
       time = 0
       results_dict[current_threshold] = []
       flag_above = False
       for current_power in power_W:
              time = time + 1

              if current_power >= current_threshold:
                   if flag_above == False:
                     time_start_higher = time
                     flag_above = True

              elif current_power <= current_threshold:
                   time_start_lower = time         
                   if flag_above == True:
                         dauer = time_start_lower - time_start_higher
                         results_dict[current_threshold].append(dauer)
                   
                         flag_above = False

#print(results_dict)


# %% 
# alleine
#Liste mit den highest values (max zeit in min) zu jedem Threshold
max_time= []
for power, times in results_dict.items():
    if times:  
        max_value = max(times)
    else:
        max_value = None  # Falls keine Werte vorhanden sind
    max_time.append({"Threshold": power, "Max Duration": max_value / 60 if max_value is not None else 0})  # Convert to minutes
max_time

# Convert the list to a DataFrame for better visualization
max_time_df = pd.DataFrame(max_time)
max_time_df

#plotten
max_time_df.plot(x='Max Duration', y='Threshold', kind='line', color='blue')
plt.ylabel('Power Threshold (W)')
plt.xlabel('Max Duration (min)')
plt.title("LEISTUNGSKURVE II")
plt.grid()

#verschönern: Shade background between each threshold, Only shade between y-ticks (blocks indicated by the y axis)
yticks = plt.gca().get_yticks()
yticks = [ytick for ytick in yticks if ytick >= 0]
num_blocks = len(yticks) - 1

for i in range(num_blocks):
       # Lightest shade at the top, darkest at the bottom (invert intensity)
       alpha = 0.1 + 0.7 * (i / max(num_blocks - 1, 1))
       plt.axhspan(
              yticks[i+1],
              yticks[i],
              color='orange',
              alpha=alpha
       )

plt.savefig("../figures/Leistungskurve II.png")
plt.show()

# %%
##Als Funktion

def get_Leistungskurve_2():
       data = load_data('data/activity.csv')
       df = pd.DataFrame(data)
       power_W = df['PowerOriginal']
       unique_power_values = power_W.unique()
       unique_power_values = sorted(unique_power_values, reverse=True)

       for current_threshold in unique_power_values:
       # gehe durch die power_W und schauen, wenn der überschritten 
              time = 0
              results_dict[current_threshold] = []
              flag_above = False
              for current_power in power_W:
                     time = time + 1

                     if current_power >= current_threshold:
                            if flag_above == False:
                                   time_start_higher = time
                            flag_above = True

                     elif current_power <= current_threshold:
                            time_start_lower = time         
                            if flag_above == True:
                                   dauer = time_start_lower - time_start_higher
                                   results_dict[current_threshold].append(dauer)
                   
                            flag_above = False

       max_time= []
       for power, times in results_dict.items():
              if times:  
                     max_value = max(times)
              else:
                     max_value = None  # Falls keine Werte vorhanden sind
              max_time.append({"Threshold": power, "Max Duration": max_value / 60 if max_value is not None else 0})  # Convert to minutes

       # Convert the list to a DataFrame for better visualization
       max_time_df = pd.DataFrame(max_time)
       #plot
       max_time_df.plot(x='Max Duration', y='Threshold', kind='line', color='blue')
       plt.ylabel('Power Threshold (W)')
       plt.xlabel('Max Duration (min)')
       plt.title("LEISTUNGSKURVE II")
       plt.grid()

#verschönern: Shade background between each threshold, Only shade between y-ticks (blocks indicated by the y axis)
       yticks = plt.gca().get_yticks()
       yticks = [ytick for ytick in yticks if ytick >= 0]
       num_blocks = len(yticks) - 1

       for i in range(num_blocks):
       # Lightest shade at the top, darkest at the bottom (invert intensity)
              alpha = 0.1 + 0.7 * (i / max(num_blocks - 1, 1))
              plt.axhspan(
                     yticks[i+1],
                     yticks[i],
                     color='orange',
                     alpha=alpha
                     )
       return 
# %%
