import os
import jsonlines
import pprint

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

# Read the English JSONL file
en_us_jsonl_file_path = os.path.join(input_folder, 'en-US.jsonl')
en_us_translations = {}
with jsonlines.open(en_us_jsonl_file_path, 'r') as reader:
    for item in reader:
        if item['partition'] == partition_to_extract:
            en_us_translations[item['id']] = item['utt']

# Loop through the JSONL files for other languages
for jsonl_file in jsonl_files:
    # Extract the language code from the file name
    lang = jsonl_file.split('.')[0]
    
    # Read the JSONL file for the current language
    jsonl_file_path = os.path.join(input_folder, jsonl_file)
    with jsonlines.open(jsonl_file_path, 'r') as reader:
        for item in reader:
            # Check if the item belongs to the specified partition ('train')
            if item['partition'] == partition_to_extract:
                # Initialize the translation dictionary for the current language if not exists
                if lang not in translations:
                    translations[lang] = {}
                
                # Use the 'id' from the current language as the key
                # and include both the translation and the English text (from "en-US" dataset)
                translation_item = {
                    item['id']: {
                        'English-Translation': en_us_translations.get(item['id'], 'Translation not found in English'),
                        'Command': item['utt']
                    }
                }
                
                translations[lang].update(translation_item)

# Save the translations as a JSON file with pretty printing
output_file = r"C:\Users\Eric\Desktop\codeamazone\outputs\en-xx.json"  # Specify the output file path
os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Create the necessary output directory
with open(output_file, 'w', encoding='utf-8') as json_file:
    pprint.pprint(translations, json_file, indent=4, sort_dicts=False)

print(f"Translations saved to '{output_file}'.")
