
import pandas as pd
import os

# Base directory for participant data
base_dir = 'C:/Users/Tomar/dev/vehicle_indoor_comfort/summer_2023/output/selected_E4_features/'
env_dir = 'C:/Users/Tomar/dev/vehicle_indoor_comfort/summer_2023/output/tinytag_data/'

# Iterate through each participant from S01 to S08
for i in range(1, 9):
    participant = f'S0{i}'
    
    # Load the .pkl file for the participant
    pkl_path = os.path.join(base_dir, f'{participant}_selected_features.pkl')
    df = pd.read_pickle(pkl_path)
    
    # Process each .env file (N1 to N5) for the participant
    merged_dfs = [df]  # Start with the main dataframe
    for n in range(1, 6):
        env_path = os.path.join(env_dir, f'{participant}_N{n}.csv')
        env_df = pd.read_csv(env_path)
        env_df['DateTime'] = pd.to_datetime(env_df['DateTime'])
        env_df.set_index('DateTime', inplace=True)
        env_df_resampled = env_df.resample('S').ffill()
        
        # Include only the timestamps that exist in the PKL file
        env_filtered = env_df_resampled[env_df_resampled.index.isin(df.index)]
        
        # Prepare CSV data for merging by renaming the columns
        env_filtered.rename(columns={col: f'{col}_N{n}' for col in env_filtered.columns}, inplace=True)
        
        # Append the filtered and column-labeled data
        merged_dfs.append(env_filtered)
    
    # Concatenate all dataframes along the columns
    final_df = pd.concat(merged_dfs, axis=1)
    
    # Interpolate to fill any gaps
    final_df.interpolate(method='linear', inplace=True)
    
    # Drop remaining rows with missing values
    final_df.dropna(inplace=True)

    # Calculate the differences in timestamps
    time_differences = final_df.index.to_series().diff().dropna()

    # Identify the breaks in df longer than 1 minute
    breaks = time_differences[time_differences > pd.Timedelta('1 minute')].index

    # Extract indices for the start and end of commuting periods
    start_indices = [final_df.index[0]] + list(breaks + pd.Timedelta('1 second'))
    end_indices = list(breaks - pd.Timedelta('1 second')) + [final_df.index[-1]]

    # Initialize the commuting column
    final_df['ID_instance'] = None

    # Assign commuting instances labels
    commute_count = 1
    for start, end in zip(start_indices, end_indices):
        final_df.loc[start:end, 'ID_instance'] = f'{participant}_{commute_count}'
        commute_count += 1
    
    # Insert 'ID_instance' column at position 1
    col_order = ['ID_instance'] + [col for col in final_df.columns if col != 'ID_instance']
    final_df = final_df[col_order]

    # Save or process final_df as needed
    outpath = 'C:/Users/Tomar/dev/vehicle_indoor_comfort/summer_2023/output/process_data'
    final_df.to_csv(f'{outpath}/{participant}_final_df.csv')

