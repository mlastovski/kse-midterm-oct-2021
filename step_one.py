first = input('name: DD/MM/YYYY: ')
second = input('name: DD/MM/YYYY: ')


date_one = first.split(':', 1)[1]


date_two = second.split(':', 1)[1]

name_one = first.split(':', 1)[0]
name_two = second.split(':', 1)[0]


date_one = date_one.replace(' ', '')
date_two = date_two.replace(' ', '')

day_one = date_one[0:2]
day_two = date_two[0:2]


month_one = date_one[3:5]
month_two = date_two[3:5]

year_one = date_one[6:10]
year_two = date_two[6:10]

if int(year_one) < int(year_two):
    print(name_one + ' is older.')
elif int(year_one) == int(year_two):
    if int(month_one) == int(month_two):
        if int(day_one) == int(day_two):
            print(name_one + ' and ' + name_two + ' are both same age.')
        elif int(day_one) < int(day_two):
            print(name_one + ' is older.')
        else:
            print(name_two + ' is older.')
    elif int(month_one) < int(month_two):
        print(name_one + ' is older.')
    else:
        print(name_two + ' is older.')
else:
    print(name_two + ' is older.')
