import os

def smallest_files(directory_path):

    with open('combined_files.txt', 'w') as f:
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as txt_file:
                    content = txt_file.read()
                if len(content.encode('utf-8')) <= 120:
                    f.write(f"Filename: {file_name}\n")
                    f.write(content + "\n")
                    f.write("-" * 50 + "\n")

smallest_files('files')
