dates = ['14-Dec', '12-Apr', '13-Apr', '31-Dec', '1-Jan', '12-Jan']

sorted_dates = sorted(dates, key=lambda date: (date.split('-')[0], date.split('-')[1][-1]))

print(sorted_dates)
