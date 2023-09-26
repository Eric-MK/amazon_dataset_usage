import os
import pandas as pd

# Specify the folder path where the JSON files are located
input_folder = r"C:\Users\Eric\Desktop\amazon-massive-dataset-1.0\1.0\data"

# Specify the folder path where you want to save the Excel files
output_folder = r"C:\Users\Eric\Desktop\codeamazone\excel_files"

# Get a list of all JSON files in the input folder
json_files = [f for f in os.listdir(input_folder) if f.endswith('.json')]

# Loop through the JSON files and convert each to an Excel file
for json_file in json_files:
    # Define the full paths for JSON and Excel files
    json_file_path = os.path.join(input_folder, json_file)
    excel_file_path = os.path.join(output_folder, json_file.replace('.json', '.xlsx'))
    
    # Initialize an empty DataFrame
    df = pd.DataFrame()

    # Read the JSON file and append its data to the DataFrame
    with open(json_file_path, 'r') as f:
        data = pd.read_json(f)
        df = df.append(data, ignore_index=True)

    # Save the DataFrame to the specified Excel file location
    df.to_excel(excel_file_path, index=False, engine='openpyxl')

    print(f"Conversion completed. Excel file '{excel_file_path}' created for '{json_file}'.")
