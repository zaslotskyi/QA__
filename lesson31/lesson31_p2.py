import re


with open('wiki_page.txt') as f:
    data = f.read()
    href_attr_values_using_re = re.findall(r'<a .*?href=\"(.+?)\"', data)
    print(href_attr_values_using_re)




