# # x = 10 -> # means commentary and does not affect code - line commentary
# #
# # """
# # block commentary for sentences
# # and descriptions ''' - also works
# # """
# #
# # point_number = 10.56
# # int_number = 5
# # print(point_number + int_number)
# #
# # string_variable = 'hello_welt'
# # string_variable2 = 'planet'
# # print(string_variable)
# # print(type(string_variable))
# # print(string_variable + '222' + string_variable2)
# # print(string_variable, '222', string_variable2)  # , add spaces
# # x, y, z, = 1, "Mada", 12.2
# # print(x)
# # print(y)
# # print(z)
# #
# # bool_value = True  # True or False for object settings
# # print(bool_value)
# #
# # non_type = None
# #
# # # calculator
# #
# # a = 100
# # b = 200
# # print(a + b + 123.123)
# #
# # # practice
# # a = 10
# # print(a)
# # print(type(a))
# # print(float(a))
# # print(a)
# # print(type(a))
# # print(bool(a))
# #
# # a = 'string'
# # print(a)
# # print(type(a))
# # print(a)
# # print(type(a))
# # print(bool(a))
# #
# # a = ''    # False if there is not text in '' or None -> cmd + / comments everything
# # print(a)
# # print(type(a))
# # print(a)
# # print(type(a))
# # print(bool(a))
# #
# # a = 123
# # b = 1.23
# # print(str(a))
# # print(str(b))
# # print(type(a))
# # print(type(str(a)))
# #
# # a = '12345'
# # b = '1234.123'
# # b = int(float(b))
# # print(b)
# # print(type(b))     # float has to be converted in (int)eger check 003_datatype_conv
# #
# # # 5 (int)eger
# # #2.5/5.0 (float)
# # # 5/2 = 2.5
# # # 5%2 = 1
# #
# name, surname, town = input('Please enter name, surname, town').split(', ')
#
# print(name)
# print(surname)
# print(town)
# #
# # # a = 1.5
# # # b = 2.5
# # # c = 3.5
# # #
# # # print(round(a))
# # # print(round(b))
# # # print(round(c))
# #
# # print(100, 2.8, True, None, 'Hello World')
# #
# # a = 100
# # b = 2.8
# # c = True
# # d = None
# # e = 'helloworld'
# #
# # print(str(a) + str(b) + str(c) + str(d) + e )   #str = string print
# #
# # a = input('Please enter something')        #input always give str
# # print(a)
# # print(type(a))
#
# # a, b, c = input('Please enter sides A, B and C. Splitwith space').split()
# # # print(a, b, c)
# # a, b, c = float(a), float(b), float(c)
# # # print(perimeter)
# # # print(type(perimeter))
# # # print(type(c))
# # # perimeter = float(a) + float(b) + float(c)
# # half_perimeter = (float(a) + float(b) + float(c)) / 2
# # triangle_area = (half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c)) ** 0.5
# # # print(perimeter)
# # # half_perimeter = perimeter / 2
# # print(half_perimeter)

name, surname, town, birth_year = input('Please enter your name, surname and town. Split with space. ').split()
print(' Hello ' + name + ' ' + surname + '. You live in ' + town + '.You are ' + str(2021 - int(birth_year)) + ' old.')


