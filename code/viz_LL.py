import pandas as pd
import matplotlib.pyplot as plt

basepath = 'C:/Users/Tomar/dev/vehicle_indoor_comfort/summer_2023/output/living_lab/LL/'

## Load the datasets
df_a = pd.read_csv(basepath+'LL_a.csv')
df_b = pd.read_csv(basepath+'LL_b.csv')
df_c = pd.read_csv(basepath+'LL_c.csv')
df_d = pd.read_csv(basepath+'LL_d.csv')
df_e = pd.read_csv(basepath+'LL_e.csv')


# Data cleaning and transformation for dataset LL_a

# Convert 'DateTime' to datetime if not already done
df_a['DateTime'] = pd.to_datetime(df_a['DateTime'])

# Handling missing values: check for NaNs
na_summary_a = df_a.isna().sum()

# Basic statistical analysis
statistics_a = df_a.describe()

na_summary_a, statistics_a

# Dictionary of datasets and their key variables
datasets = {
    'LL_a.csv': df_a,
    'LL_b.csv': df_b,
    'LL_c.csv': df_c,
    'LL_d.csv': df_d,
    'LL_e.csv': df_e
}

# Correct figure for multiple subplots based on updated column names
fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(14, 25))

# Update the correct column names and variable pairing
plot_vars_corrected = {
    'LL_a.csv': [('Temp_Air(C)', 0), ('Illu(lx)', 1)],
    'LL_b.csv': [('Temp_Globe(C)', 2), ('WBGT(C)', 3)],
    'LL_c.csv': [('CO2', 4), ('Temp_Globe(C)', 5)],
    'LL_d.csv': [('Temp_Air(C)_x', 6), ('RH(%)', 7)],
    'LL_e.csv': [('Temp_Air(C)', 8), ('TNW', 9)]
}

# Redo histograms with corrected variable names
for file_name, var_index_pairs in plot_vars_corrected.items():
    for var, index in var_index_pairs:
        ax = axes[index // 2, index % 2]
        data = datasets[file_name]
        # Filter out placeholder values, if necessary
        if var in ['WBGT(C)', 'RH(%)'] and (data[var] < -999).any():
            data_to_plot = data[data[var] > -999][var]
        else:
            data_to_plot = data[var]
        ax.hist(data_to_plot, bins=50, color='skyblue', edgecolor='black')
        ax.set_title(f'Distribution of {var} in {file_name}')
        ax.set_xlabel(var)
        ax.set_ylabel('Frequency')

fig.tight_layout()
plt.show()


# Creating visualizations for LL_a

# Time Series Plot for Temp_Air and Illu
fig, ax1 = plt.subplots(figsize=(14, 7))

color = 'tab:red'
ax1.set_xlabel('DateTime')
ax1.set_ylabel('Temp_Air (°C)', color=color)
ax1.plot(df_a['DateTime'], df_a['Temp_Air(C)'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Illu (lx)', color=color)
ax2.plot(df_a['DateTime'], df_a['Illu(lx)'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Time Series of Air Temperature and Illumination (LL_a)')
fig.tight_layout()

# Scatter Plot for Temp_Air vs Illu
plt.figure(figsize=(10, 6))
plt.scatter(df_a['Temp_Air(C)'], df_a['Illu(lx)'], alpha=0.5)
plt.title('Scatter Plot of Temp_Air vs. Illu (LL_a)')
plt.xlabel('Temp_Air (°C)')
plt.ylabel('Illu (lx)')
plt.grid(True)

plt.show()


# Data cleaning and transformation for dataset LL_b
# df_b = pd.read_csv(basepath+'LL_b.csv')

# Convert 'DateTime' to datetime if not already done
df_b['DateTime'] = pd.to_datetime(df_b['DateTime'])

# Handling missing or placeholder values: filter out -999999 from 'WBGT(C)' if it exists
df_b_filtered = df_b[df_b['WBGT(C)'] > -999999]

# Creating visualizations for LL_b

# Time Series Plot for Temp_Globe and WBGT
fig, ax1 = plt.subplots(figsize=(14, 7))

color = 'tab:red'
ax1.set_xlabel('DateTime')
ax1.set_ylabel('Temp_Globe (°C)', color=color)
ax1.plot(df_b_filtered['DateTime'], df_b_filtered['Temp_Globe(C)'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('WBGT (°C)', color=color)
ax2.plot(df_b_filtered['DateTime'], df_b_filtered['WBGT(C)'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Time Series of Globe Temperature and WBGT (LL_b)')
fig.tight_layout()
plt.show()


# Data cleaning and transformation for dataset LL_c
# df_c = pd.read_csv(basepath+'LL_c.csv')

# Convert 'DateTime' to datetime if not already done
df_c['DateTime'] = pd.to_datetime(df_c['DateTime'])

# No placeholders identified previously for CO2 or Temp_Globe, but let's check and proceed
df_c_filtered = df_c

# Creating visualizations for LL_c

# Time Series Plot for CO2 and Temp_Globe
fig, ax1 = plt.subplots(figsize=(14, 7))

color = 'tab:red'
ax1.set_xlabel('DateTime')
ax1.set_ylabel('CO2 (ppm)', color=color)
ax1.plot(df_c_filtered['DateTime'], df_c_filtered['CO2'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Temp_Globe (°C)', color=color)
ax2.plot(df_c_filtered['DateTime'], df_c_filtered['Temp_Globe(C)'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Time Series of CO2 and Globe Temperature (LL_c)')
fig.tight_layout()
plt.show()


# Data cleaning and transformation for dataset LL_d
# df_d = pd.read_csv(basepath+'LL_d.csv')

# Convert 'DateTime' to datetime if not already done
df_d['DateTime'] = pd.to_datetime(df_d['DateTime'])

# Handling missing or placeholder values: filter out -999999 from 'RH(%)' if it exists
df_d_filtered = df_d[df_d['RH(%)'] > -999999]

# Creating visualizations for LL_d

# Time Series Plot for Temp_Air and RH
fig, ax1 = plt.subplots(figsize=(14, 7))

color = 'tab:red'
ax1.set_xlabel('DateTime')
ax1.set_ylabel('Temp_Air (°C)', color=color)
ax1.plot(df_d_filtered['DateTime'], df_d_filtered['Temp_Air(C)_x'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('RH (%)', color=color)
ax2.plot(df_d_filtered['DateTime'], df_d_filtered['RH(%)'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Time Series of Air Temperature and Relative Humidity (LL_d)')
fig.tight_layout()
plt.show()


# Data cleaning and transformation for dataset LL_e
# df_e = pd.read_csv(basepath+'LL_e.csv')

# Convert 'DateTime' to datetime if not already done
df_e['DateTime'] = pd.to_datetime(df_e['DateTime'])

# Creating visualizations for LL_e

# Time Series Plot for Temp_Air and TNW
fig, ax1 = plt.subplots(figsize=(14, 7))

color = 'tab:red'
ax1.set_xlabel('DateTime')
ax1.set_ylabel('Temp_Air (°C)', color=color)
ax1.plot(df_e['DateTime'], df_e['Temp_Air(C)'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('TNW', color=color)  # Assuming TNW is a temperature-related measure without placeholders
ax2.plot(df_e['DateTime'], df_e['TNW'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Time Series of Air Temperature and TNW (LL_e)')
fig.tight_layout()
plt.show()

