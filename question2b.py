import os
import jsonlines
import json
from pprint import pprint

# Specify the folder path where the original JSONL files are located (the dataset directory)
input_folder = r"C:\Users\Eric\Desktop\amazon-massive-dataset-1.0\1.0\data"

# List all JSONL files in the dataset directory
jsonl_files = [f for f in os.listdir(input_folder) if f.endswith('.jsonl')]

# Initialize a dictionary to store translations from 'en-US' to other languages
translations = {}

# Specify the pivot language as 'en-US'
pivot_language = 'en-US'

# Specify the partition to extract (e.g., 'train')
partition_to_extract = 'train'

# Loop through the JSONL files
for jsonl_file in jsonl_files:
    # Extract the language code from the file name
    lang = jsonl_file.split('.')[0]
    
    # Read the JSONL file for the current language
    jsonl_file_path = os.path.join(input_folder, jsonl_file)
    with jsonlines.open(jsonl_file_path, 'r') as reader:
        for item in reader:
            # Check if the item belongs to the specified partition ('train')
            if item['partition'] == partition_to_extract:
                # Extract the 'id' and 'utt' fields
                command_id = item['id']
                english_text = item['utt']
                
                # Initialize the translation dictionary for the current language if not exists
                if lang not in translations:
                    translations[lang] = {}
                
                # For all languages, use the English command ID and text as the translation
                translations[lang][command_id] = {
                    "English": english_text,
                    "Translation": english_text
                }

# Save the translations as a JSON file with pretty printing
output_file = r"C:\Users\Eric\Desktop\codeamazone\outputs\en-xx.json"  # Specify the output file path
os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Create the necessary output directory
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(translations, json_file, indent=4, ensure_ascii=False)

print(f"Translations saved to '{output_file}'.")
