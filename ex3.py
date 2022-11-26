# х + у +  -- 1ч
# х + у -  -- 4ч
# х - у +  -- 2ч
# х - у -  -- 3ч

x = int(input('Enter x num '))
y = int(input('Enter y num '))

if x in range(0, 1000) and y in range(0, 1000):
    print('1st quater')
elif x in range(0, 1000) and y in range(-1000, 0):
    print('4th quater')
elif x in range(-1000, 0) and y in range(0, 1000):
    print('2nd quater')
elif x in range(-1000, 0) and y in range(-1000, 0):
    print('3rd quater')

# a = -3
# b = 2
# if a in range(-10000, 0):
#     print(True)
# elif b in range(0, 10000):
#     print('Also True')
