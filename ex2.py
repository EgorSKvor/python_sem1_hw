for x in range(2):
    for y in range(2):
        for z in range(2):
            for x1 in range(2):
                for y1 in range(2):
                    for z1 in range(2):
                        # если убрать скобки у not x1, то not подчеркивает как ошибку и программа не выполняется
                        if not (x or y or z) == (not x1) and not y1 and not z1:
                            print("Истина при х=", x, " y=", y, " z=",
                                  z, " х1=", x1, " y1=", y1, " z1=", z1)
                            # print('При значении x = ',x, 'при значении у = ',y, 'при значении z = ',z 'уравнение -(Х или У или Z) = -X и -У и -Z - истинно');
print('В остальных случаях - ЛОЖНО')
