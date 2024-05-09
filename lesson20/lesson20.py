def longest_line_in_file(file):
    with open(file, "r") as file:
        max_length = 0
        longest_line = ""
        for line in file:
            if len(line.strip()) >= max_length:
                max_length = len(line.strip())
                longest_line = line.strip()
    return longest_line

print(longest_line_in_file('lesson20file.txt'))
