def adult_users(users):
    names = []

    for i in users:
        if i['age'] >= 18:
            names.append(i['name'])

    return names

# print(adult_users([
#     {'name': 'Luarvik L. Luarvik',
#      'age': 17},
#     {'name': 'Olaf Andvarafors',
#      'age': 18},
#     {'name': 'Brun Du Barnstokr',
#      'age': 19}
# ]))

assert adult_users([{'name': 'Luarvik L. Luarvik','age': 17},{'name': 'Olaf Andvarafors','age': 18},{'name': 'Brun Du Barnstokr','age': 19}]) == ['Olaf Andvarafors', 'Brun Du Barnstokr']
print('Passed')