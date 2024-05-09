def longest_line_in_file(file):
    with open(f"{file}", "r") as file:
        max_length = 0
        longest_line = ""
        for line in file:
            if len(line) > max_length:
                max_length = len(line)
                longest_line = line
    return longest_line

print(longest_line_in_file('lesson20file.txt'))

