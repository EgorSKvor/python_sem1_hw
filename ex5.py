import math
numA_X = abs(int(input('Enter X of first num ')))
numA_Y = abs(int(input('Enter Y of first num ')))
numB_X = abs(int(input('Enter X of second num ')))
numB_Y = abs(int(input('Enter Y of second num ')))

if numB_Y in range(0, 1000) and numA_Y in range(0, 1000):
    if numA_Y > numB_Y:
        kat2 = numA_Y - numB_Y
    elif numA_Y < numB_Y:
        kat2 = numB_Y - numA_Y
    else:
        kat2 = numA_Y + numB_Y


kat1 = numA_X + numB_X
dist = math.sqrt(kat1*kat1 + kat2*kat2)
print(numB_X, numB_Y)
print(kat1, kat2)
print(f'Distance = {dist}')


# for i in range(4):
#     li = int(input('Enter coordinates '))
# if li[1] in range(0, 1000) and li[3] in range(0, 1000):
#     if li[1] > li[3]:
#         kat2 = li[1] - li[3]
#     else:
#         kat2 = li[3] - li[1]
# kat1 = li[0] + li[2]
# dist = math.sqrt(kat1*kat1 + kat2*kat2)
# print(dist)
