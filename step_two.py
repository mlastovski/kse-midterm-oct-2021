weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
i = input('Enter a day of the week and number of days: ').split()
e = int(i[-1])
starting_point = weekdays.index(i[0])
a = e + starting_point - len(weekdays)
print(weekdays[a])