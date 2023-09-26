import os
import pandas as pd
import jsonlines

# Specify the folder path where the JSONL files are located
input_folder = r"C:\Users\Eric\Desktop\amazon-massive-dataset-1.0\1.0\data"

# Specify the folder path where you want to save the Excel files
output_folder = r"C:\Users\Eric\Desktop\codeamazone\excel_files"

# Get a list of all JSONL files in the input folder
jsonl_files = [f for f in os.listdir(input_folder) if f.endswith('.jsonl')]

# Loop through the JSONL files and convert each to an Excel file
for jsonl_file in jsonl_files:
    # Define the full paths for JSONL and Excel files
    jsonl_file_path = os.path.join(input_folder, jsonl_file)
    excel_file_path = os.path.join(output_folder, jsonl_file.replace('.jsonl', '.xlsx'))
    
    # Initialize an empty list to store data
    data_list = []

    try:
        # Read the JSON Lines file using jsonlines
        with jsonlines.open(jsonl_file_path, 'r') as reader:
            for item in reader:
                data_list.append(item)

        # Create a DataFrame from the list of data
        df = pd.DataFrame(data_list)

        # Save the DataFrame to the specified Excel file location
        df.to_excel(excel_file_path, index=False, engine='openpyxl')

        print(f"Conversion completed. Excel file '{excel_file_path}' created for '{jsonl_file}'.")
    except Exception as e:
        print(f"An error occurred while processing '{jsonl_file}': {str(e)}")
