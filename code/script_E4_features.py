# -*- coding: utf-8 -*-
"""
@author: Tomar P.

"""

import os
import pandas as pd
import flirt
import argparse

def process_E4(dataset_path, output_directory):
    
    # Create the output directory if it does not exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Iterate over each subject folder in the specified directory path
    for subject_dir in os.listdir(dataset_path):
        subject_path = os.path.join(dataset_path, subject_dir)

        # Check if it's a directory
        if os.path.isdir(subject_path):
            # Initialize an empty DataFrame to store the combined data for the subject
            combined_data = pd.DataFrame()

            # Iterate over E4 zip files in the 'E4' folder
            E4_dir_path = os.path.join(subject_path, 'E4')
            if os.path.exists(E4_dir_path):
                E4_zip_files = [f for f in os.listdir(E4_dir_path) if f.endswith('.zip')]

                for E4_zip_file in E4_zip_files:
                    try:
                        # Construct the full path to the E4 zip file
                        E4_zip_path = os.path.join(E4_dir_path, E4_zip_file)

                        # Process the data from the current E4 zip file
                        data = flirt.with_.empatica(E4_zip_path,
                                                    window_length=60,
                                                    window_step_size=1,
                                                    hrv_features=True,
                                                    eda_features=True,
                                                    acc_features=True)

                        # Check if the data is not empty before concatenating
                        if not data.empty:
                            combined_data = pd.concat([combined_data, data])
                        else:
                            print(f"Skipping empty file: {E4_zip_file}")

                    except Exception as e:
                        print(f"Error processing file {E4_zip_file}: {e}")
                        

            # Convert DateTime index to UTC and remove the timezone offset
            combined_data.index = combined_data.index.tz_localize(None)
            # Rename the index column to "DateTime"
            combined_data.index.name = "DateTime"
            
            # Save the combined_data DataFrame to a CSV file for the current subject
            subject_save_path = os.path.join(output_directory, f'{subject_dir}_features.pkl')
            # combined_data.to_csv(subject_save_path, index=True)
            combined_data.to_pickle(subject_save_path)
            print(f"Result data saved to: {subject_save_path}")

def main():
    parser = argparse.ArgumentParser(description='Process E4 data in a directory and save the results.')
    parser.add_argument('--data', dest='dataset_path', help='Path to the directory containing subject data.')
    parser.add_argument('--output', dest='output_directory', help='Path to the directory to save output files.')
    args = parser.parse_args()

    process_E4(args.dataset_path, args.output_directory)

if __name__ == "__main__":
    main()

