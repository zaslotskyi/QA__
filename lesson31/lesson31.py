href_list = []
start = 0

with open('wiki_page.txt') as f:
    data = f.read()
    while True:
        start_link = data.find('<a href="', start)
        if start_link == -1:
            break
        start_quote = start_link + len('<a href="')
        end_quote = data.find('"', start_quote)
        href = data[start_quote:end_quote]
        href_list.append(href)
        start = end_quote + 1

    print(href_list)



