import os
import jsonlines

# Specify the folder path where the original JSONL files are located
input_folder = r"C:\Users\Eric\Desktop\amazon-massive-dataset-1.0\1.0\data"

# Create a dictionary to store the output folder paths for each language
output_folders = {
    'en-US': r"C:\Users\Eric\Desktop\codeamazone\outputs\en-US",
    'sw-KE': r"C:\Users\Eric\Desktop\codeamazone\outputs\sw-KE",
    'de-DE': r"C:\Users\Eric\Desktop\codeamazone\outputs\de-DE"
}

# Define the languages and partitions you want to generate
languages = ['en-US', 'sw-KE', 'de-DE']
partitions = ['test', 'train', 'dev']

# Loop through languages and partitions
for lang in languages:
    for partition in partitions:
        # Define the output JSONL file path
        output_file_path = os.path.join(output_folders[lang], f'{lang}-{partition}.jsonl')

        # Create the output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Filter and write data to the output JSONL file
        with jsonlines.open(output_file_path, 'w') as writer:
            with jsonlines.open(os.path.join(input_folder, f'{lang}.jsonl'), 'r') as reader:
                for item in reader:
                    if item['partition'] == partition:
                        writer.write(item)

print("JSONL files generated for English, Swahili, and German partitions.")
