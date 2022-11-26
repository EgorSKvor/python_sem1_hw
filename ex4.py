# х + у +  -- 1ч
# х + у -  -- 4ч
# х - у +  -- 2ч
# х - у -  -- 3ч

numX = int(input('Enter num x '))
numY = int(input('Enter num y '))
if numX in range(0, 1000) and numY in range(0, 1000):
    print('1st quater')
elif numX in range(0, 1000) and numY in range(-1000, 0):
    print('4th quater')
elif numX in range(-1000, 0) and numY in range(0, 1000):
    print('2nd quater')
if numX in range(-1000, 0) and numY in range(-1000, 0):
    print('3st quater')
