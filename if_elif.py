id_code = input('Please enter ID: ')
if len(id_code) == 11:
    if id_code[0] != '3' and id_code[0] !='4':
        print('Your ID code is wrong')

    print('Your ID code is: ' + id_code)
elif len(id_code) > 11:
    print('Your ID is too long')
else:
    print('Your ID is too short')