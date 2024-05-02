# -*- coding: utf-8 -*-
"""
@author: Tomar P. 

TODO: select featues from the E4 features
TODO: save each subject as selected_features.pkl

"""

import os
import pandas as pd
import argparse

def read_features(features_dir, output_dir):
    # List of selected features
    hrv_features = ['hrv_vlf', 'hrv_lf', 'hrv_hf', 'hrv_sdnn', 'hrv_rmssd', 'hrv_mean_nni', 
                    'hrv_median_nni', 'hrv_range_nni', 'hrv_entropy'
                    ]
    eda_features = ['eda_tonic_mean', 'eda_tonic_std', 'eda_tonic_sum','eda_tonic_energy','eda_phasic_mean',
                    'eda_phasic_std', 'eda_phasic_sum', 'eda_phasic_energy'
                    ]
    acc_features = ['acc_acc_x_min', 'acc_acc_y_min', 'acc_acc_z_min', 'acc_l2_min', 'acc_acc_x_max', 
                    'acc_acc_y_max', 'acc_acc_z_max', 'acc_l2_max', 'acc_acc_x_ptp', 'acc_acc_y_ptp', 
                    'acc_acc_z_ptp', 'acc_l2_ptp'
                    ]

    # Combine all selected columns into a single list
    selected_features = hrv_features + eda_features + acc_features
    
    # Iterate over each subject in the features directory
    for filename in os.listdir(features_dir):
        # Check if the file is a Pickle file
        if filename.endswith('_features.pkl'):
            # Construct the full path to the Pickle file
            file_path = os.path.join(features_dir, filename)
            # Read the Pickle file into a DataFrame
            df = pd.read_pickle(file_path)
            # Select the desired features columns
            selected_df = df[selected_features]
            # Construct the output file path
            output_file = os.path.join(output_dir, filename.replace('_features.pkl', '_selected_features.pkl'))
            # Save the selected features to CSV
            selected_df.to_pickle(output_file)
            print(f"Selected features saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Read E4 features pkl files and filter selected features. Save selected features in a directory as subject_id_selected_features.pkl.')
    parser.add_argument('--features', dest='features_dir', help='Path to the directory containing features Pickle files.')
    parser.add_argument('--output', dest='output_dir', help='Path to the directory to save selected features CSV files.')
    args = parser.parse_args()

    # Read features from the specified directory
    read_features(args.features_dir, args.output_dir)

if __name__ == "__main__":
    main()
