months = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

dates = ['14-Dec', '12-Apr', '13-Apr', '31-Dec', '1-Jan', '12-Jan', '10-Dec', '7-Aug']

sorted_dates = sorted(dates, key=lambda x: (months[x.split('-')[1]], int(x.split('-')[0])))
print(sorted_dates)
