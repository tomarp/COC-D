# -*- coding: utf-8 -*-
"""
@author: Tomar P.

TODO: Process tinytag sensors data
TODO: Combine data for N1, N2, N3, N4, N5
    
"""

import os
import pandas as pd
import argparse

def clean_units(value):
    """Remove specific characters from the data values."""
    if isinstance(value, str):
        return value.replace('°C', '').replace('%RH', '').strip()
    return value

def process_tinytag(dataset_path, output_directory):
    for subject_dir in os.listdir(dataset_path):
        subject_path = os.path.join(dataset_path, subject_dir)
        if os.path.isdir(subject_path):
            for pattern in ['N1', 'N2', 'N3', 'N4', 'N5']:
                pattern_files = [f for f in os.listdir(os.path.join(subject_path, 'tinytag')) if f.startswith(pattern)]
                pattern_data = pd.DataFrame()

                for pattern_file in pattern_files:
                    file_path = os.path.join(subject_path, 'tinytag', pattern_file)
                    df = pd.read_csv(file_path, header=None, index_col=None, encoding='latin-1')
                    df = df.iloc[5:, 1:]  # Remove first five rows and first column
                    df = df.rename(columns={1: 'DateTime', 2: 'Temp(C)', 3: 'RH(%)', 4: 'Dewpoint(C)'})  # Rename columns
                    
                    # Apply the clean_units function to the necessary columns
                    df['Temp(C)'] = df['Temp(C)'].apply(clean_units).astype(float)
                    df['RH(%)'] = df['RH(%)'].apply(clean_units).astype(float)
                    df['Dewpoint(C)'] = df['Dewpoint(C)'].apply(clean_units).astype(float)

                    pattern_data = pd.concat([pattern_data, df])

                pattern_data = pattern_data.set_index('DateTime')
                output_file = os.path.join(output_directory, f'{subject_dir}_{pattern}.csv')
                pattern_data.to_csv(output_file)
                print(f"Aggregated data for {subject_dir}_{pattern} saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Process tinytag sensor data in a directory and aggregate as separate files for each subject and pattern.')
    parser.add_argument('--data', dest='dataset_path', help='Path to the directory containing subject data.')
    parser.add_argument('--output', dest='output_directory', help='Path to the directory to save aggregated CSV files.')
    args = parser.parse_args()

    process_tinytag(args.dataset_path, args.output_directory)

if __name__ == "__main__":
    main()
