# -*- coding: utf-8 -*-
"""
@author: Tomar P.

"""

import os
import pandas as pd


### Process nodes files

def process_tsv_file(filepath):
    df = pd.read_csv(filepath, sep='\t', header=None, skiprows=36)
    return df

# Define a dictionary with node IDs as keys and lists of column names as values
column_names = {
    '19F798E': ['Node_ID', 'DateTime', 'Status', 'Bi1', 'Connection', 'Temp_Air(C)', 'Illu(lx)', 'Ele1(A)', 'Ele2(A)', 'Bi2', 'Door', 'Window'],  
    '19F7993': ['Node_ID', 'DateTime', 'Status', 'Bi1', 'Connection', 'Temp_Air(C)', 'Illu(lx)', 'Ele1(A)', 'Ele2(A)', 'Bi2', 'Window', 'Door'],  
    '1A057E0': ['Node_ID', 'DateTime', 'Status', 'Bi1', 'Connection', 'Temp_Air(C)', 'Illu(lx)', 'Ele1(A)', 'Ele2(A)', 'Bi2', 'Door', 'Window'],
    '1A057E5': ['Node_ID', 'DateTime', 'Status', 'Bi1', 'Connection', 'Temp_Air(C)', 'Illu(lx)', 'Ele1(A)', 'Ele2(A)', 'Bi2', 'Door', 'Window'],
    '1A00DBE': ['Node_ID', 'DateTime', 'Status', 'Bi1', 'Connection', 'Temp_Air(C)', 'Illu(lx)', 'Ele1(A)', 'Ele2(A)', 'Bi2', 'Window', 'Door'], 
    '1A00DC1': ['Node_ID', 'DateTime', 'Status', 'Bi1', 'Connection', 'CO2', 'Temp_Air(C)', 'RH(%)', 'Temp_Globe(C)', 'Bi2', 'x', 'x'], 
    '19FD06D': ['Node_ID', 'DateTime', 'Status', 'Bi1', 'Connection', 'CO2', 'Temp_Air(C)', 'RH(%)', 'Temp_Globe(C)', 'Bi2', 'x', 'x'], 
    '1A057DF': ['Node_ID', 'DateTime', 'Status', 'Bi1', 'Connection', 'CO2', 'Temp_Air(C)', 'RH(%)', 'Temp_Globe(C)', 'Bi2', 'x', 'x'] 
    }

nodes = {'19F798E', '19F7993', '19FD06D', '1A057E5', '1A00DC1', '1A00DBE', '1A057DF', '1A057E0'}

basepath = 'path/datasets/living_lab_2023/'  
outpath = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/'

def node_data(basepath, nodes, outpath, column_names):
    node_data = {node: [] for node in nodes}
    tsv_files = [file for file in os.listdir(basepath) if file.endswith('.tsv')]
    
    for tsv_file in tsv_files:
        filepath = os.path.join(basepath, tsv_file)
        df = process_tsv_file(filepath)
        print(f"Processed data for file: {tsv_file}")
        
        for node in nodes:
            node_df = df[df[0] == node]  
            if node in column_names:
                node_df.columns = column_names[node]  
                cols = node_df.columns.tolist()
                cols = [cols[1]] + cols[0:1] + cols[2:]
                node_df = node_df[cols]
                
            node_data[node].append(node_df)
    
    for node, dfs in node_data.items():
        if not dfs:
            continue
        node_df = pd.concat(dfs, ignore_index=True)
        node_filepath = os.path.join(outpath, f"node_{node}.csv")
        node_df.to_csv(node_filepath, index=False)

# Call the function
node_data(basepath, nodes, outpath, column_names)


### Process S02, S06, S08 LL data file

def transform_row(input_row):
    parts = input_row.split(',')
    corrected_parts = [parts[0]]  
    i = 1
    while i < len(parts):
        if parts[i] == "-999999" or parts[i] == "0":
            corrected_parts.append(parts[i])
            i += 1  
        elif i + 1 < len(parts) and parts[i+1].isdigit():
            decimal_number = f"{parts[i]}.{parts[i+1]}"
            corrected_parts.append(decimal_number)
            i += 2  
        else:
            corrected_parts.append(parts[i])
            i += 1  
    output_row = ','.join(corrected_parts)
    return output_row

def transform_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            transformed_line = transform_row(line.strip())
            output_file.write(transformed_line + '\n')

def process_files(input_files, output_folder):
    for input_file_path in input_files:
        # Construct output file path
        file_name = os.path.basename(input_file_path)
        output_file_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.csv")
        
        transform_file(input_file_path, output_file_path)
        
        df = pd.read_csv(output_file_path)
        columns_to_drop = [6, 12, 14]
        df.drop(df.columns[columns_to_drop], axis=1, inplace=True)
        
        # Rename columns
        column_names = ['DateTime', 'Temp_Globe(C)', 'TNW', 'Temp_Air(C)', 'RH(%)', 'Air_Velocity(m/s)', 'WBGT(C)', 'WBGTsi(C)', 'HI(C)', 'HX(C)', 'PMV(C)', 'PPD']
        df.columns = column_names
        
        df.to_csv(output_file_path, index=False)

# Specify input and output folder paths
input_folder = 'path/datasets/living_lab_2023'
output_folder = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab'

# List input files
input_files = [
    os.path.join(input_folder, 'S06.txt'),
    os.path.join(input_folder, 'S02.txt'),
    os.path.join(input_folder, 'S08.txt')
]

# Process files
process_files(input_files, output_folder)

################################################
### Correct DateTime format

def try_parsing_date(text):
   
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S"):  # Add more formats here as needed
        try:
            return pd.to_datetime(text, format=fmt)
        except ValueError:
            continue
    raise ValueError("no valid date format found")

def convert_all_files_in_folder(folder_path, output_folder):
    """
    Convert datetime format for all files in a given folder.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):  
            file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(output_folder, filename)

            # Load the file
            df = pd.read_csv(file_path)

            # Attempt to convert the DateTime column
            df['DateTime'] = df['DateTime'].apply(try_parsing_date)
            df['DateTime'] = df['DateTime'].dt.strftime("%Y-%m-%d %H:%M:%S")

            # Save the converted file
            df.to_csv(output_file_path, index=False)

            print(f"Processed {filename}")

folder_path = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/'
output_folder = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/final/'
convert_all_files_in_folder(folder_path, output_folder)


### Nodes data into LL and filter

###########################################################
## Living Lab 15

file_path0 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/final/node_19F798E.csv'

# Load the data
data0 = pd.read_csv(file_path0)

    
# Assuming 'DateTime' is present in both datasets, convert them to datetime type for proper merging
data0['DateTime'] = pd.to_datetime(data0['DateTime'])
    

# Selecting only the required columns to create a new DataFrame as specified
required_columns = ['DateTime', 'Temp_Air(C)', 'Illu(lx)', 'Ele1(A)', 'Ele2(A)', 'Window', 'Door' ]
LL15 = data0[required_columns]


path0 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/LL/LL15.csv'
LL15.to_csv(path0, index=False)


###############################################################
## Living Lab 16

file_path1 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/final/node_19F7993.csv'
file_path2 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/final/node_19FD06D.csv'

data1 = pd.read_csv(file_path1)
data2 = pd.read_csv(file_path2)
    
data1['DateTime'] = pd.to_datetime(data1['DateTime'])
data2['DateTime'] = pd.to_datetime(data2['DateTime'])
    
combined_LL16 = pd.merge(data1, data2, on='DateTime', how='outer')

required_columns = ['DateTime', 'CO2', 'RH(%)', 'Temp_Globe(C)', 'Temp_Air(C)_x', 'Illu(lx)', 'Ele1(A)', 'Ele2(A)', 'Window', 'Door' ]
LL16 = combined_LL16[required_columns]

path1 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/LL/LL16.csv'
LL16.to_csv(path1, index=False)


#############################################################
## Living Lab 17

file_path3 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/final/node_1A057E5.csv'
file_path4 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/final/node_1A00DC1.csv'

data3 = pd.read_csv(file_path3)
data4 = pd.read_csv(file_path4)
    
data3['DateTime'] = pd.to_datetime(data3['DateTime'])
data4['DateTime'] = pd.to_datetime(data4['DateTime'])
    
combined_LL17 = pd.merge(data3, data4, on='DateTime', how='outer')

required_columns = ['DateTime', 'CO2', 'RH(%)', 'Temp_Globe(C)', 'Temp_Air(C)_x', 'Illu(lx)', 'Ele1(A)', 'Ele2(A)', 'Window', 'Door' ]
LL17 = combined_LL17[required_columns]

path2 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/LL/LL17.csv'
LL17.to_csv(path2, index=False)


##################################################################
## Living Lab 18

file_path5 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/final/node_1A00DBE.csv'
file_path6 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/final/node_1A057DF.csv'

data5 = pd.read_csv(file_path5)
data6 = pd.read_csv(file_path6)
    
data5['DateTime'] = pd.to_datetime(data5['DateTime'])
data6['DateTime'] = pd.to_datetime(data6['DateTime'])
    
combined_LL18 = pd.merge(data5, data6, on='DateTime', how='outer')

required_columns = ['DateTime', 'CO2', 'RH(%)', 'Temp_Globe(C)', 'Temp_Air(C)_x', 'Illu(lx)', 'Ele1(A)', 'Ele2(A)', 'Window', 'Door' ]
LL18 = combined_LL18[required_columns]

path3 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/LL/LL18.csv'
LL18.to_csv(path3, index=False)


###############################################################
## Living Lab 19

file_path7 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/final/node_1A057E0.csv'

data7 = pd.read_csv(file_path7)
    
data7['DateTime'] = pd.to_datetime(data7['DateTime'])

required_columns = ['DateTime', 'Temp_Air(C)', 'Illu(lx)', 'Ele1(A)', 'Ele2(A)', 'Window', 'Door' ]
LL19 = data7[required_columns]

path4 = 'path/vehicle_indoor_comfort/summer_2023/output/living_lab/LL/LL19.csv'
LL19.to_csv(path4, index=False)

