numbers = [num for num in range(1, 10)]

for num in numbers:
    if num == 1:
        print('\n' + str(num)+'st')
    elif num == 2:
        print('\n' + str(num)+'nd')
    elif num == 3:
        print('\n' + str(num)+'rd')
    else:
        print('\n' + str(num)+'th')
