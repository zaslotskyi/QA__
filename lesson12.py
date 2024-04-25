string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."

split_string = string.split()
edited_list = []

for i in split_string:
    if "oo" in i or "OO" in i:
        edited_list.append(i.title())

formatted_list_to_string = ' '.join(map(str, edited_list))

print(formatted_list_to_string)

