def smallest_files(dict_data):

    with open('combined_files.txt', 'w') as f:
        for filename, content in dict_data.items():
            if len(content.encode('utf-8')) <= 120:
                f.write(f"Filename: {filename}\n")
                f.write(content + "\n")
                f.write("-" * 50 + "\n")




smallest_files({
    'file1.txt': 'You have source_directory with nested directories (any level of nesting). '
                 'In all those directories could be text files (with extension *.txt) and any other files.'
                 'Create file combined_files.txt.',
    'file2.txt': 'You have source_directory with nested directories (any level of nesting).'
                 'testtesttest',
    'file3.txt': 'You have source_directory with nested directories (any level of nesting).'

})
