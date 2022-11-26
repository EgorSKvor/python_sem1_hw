l = 5
for i in range(l):
    day = int(input('Enter day of the week '))
    if 1 <= day < 7:
        if day > 5:
            print(f'This is weekend {day} uhuuuuuuu')
        else:
            print(f'This is weekday (((')
    else:
        print('Enter day of the week between Monday(1) and Sunday(7)')
    break
