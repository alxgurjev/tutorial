# a = 'Your salary is'
# b = 1000
# c = 2000
# d = 3000
# new_string = a + ' ' + str(b)
# formatted_string = 'your salary is {2}, or {1}, or {0}'
#
# print(new_string)
# print(formatted_string.format(b, c, d))

a = 'your salary is'
b = 1000
c = None
d = True
formatted_string = 'This is {product:}. It costs {price:}'
print(formatted_string.format(product='computer', price=350.00))

emp_name = 'John'
emp_age = 30
emp_salary = 1500

emp_string = f'Hello my name is {emp_name}. I am {emp_age} years old. My salary is {emp_salary}'
print(emp_string)

some_string = 'Alejandro that\'s my name'
print(some_string)

some_string = 'Hello\nBrave\nNew\nWorld'
print(some_string)