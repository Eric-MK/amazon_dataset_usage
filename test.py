import os
import pandas as pd

# Specify the folder path where the Excel files are located
input_folder = r"C:\Users\Eric\Desktop\codeamazone\excel_files"

# Create an empty DataFrame to store merged data
merged_df = pd.DataFrame(columns=['id', 'utt', 'annot_utt'])

# Read the English data into a DataFrame (assuming the English file is named 'en-xx.xlsx')
english_file_path = os.path.join(input_folder, 'en-US.xlsx')
english_df = pd.read_excel(english_file_path)

# Filter the English data to keep only the columns 'id', 'utt', 'annot_utt'
english_df = english_df[['id', 'utt', 'annot_utt']]

# Iterate through the Excel files in the input folder
for excel_file in os.listdir(input_folder):
    if excel_file.endswith('.xlsx') and excel_file != 'en-US.xlsx':
        # Read the data from the current Excel file
        excel_file_path = os.path.join(input_folder, excel_file)
        language_df = pd.read_excel(excel_file_path)
        
        # Filter the data for the current language and columns 'id', 'utt', 'annot_utt'
        language_df = language_df[['id', 'utt', 'annot_utt']]
        
        # Merge the language-specific data into the merged DataFrame based on the 'id' column
        merged_df = pd.merge(merged_df, language_df, on='id', how='left', suffixes=('', f'_{excel_file[:-5]}'))

# Merge the English data with the merged data based on the 'id' column
merged_df = pd.merge(merged_df, english_df, on='id', how='left', suffixes=('', '_en'))

# Save the merged data to "en-xx.xlsx"
merged_excel_file_path = os.path.join(input_folder, 'en-xx.xlsx')
merged_df.to_excel(merged_excel_file_path, index=False, engine='openpyxl')

print(f"Excel file '{merged_excel_file_path}' created with merged data from all languages.")
