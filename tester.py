# some_string = ''
# print(type(some_string))

string_sample = 'Hello world world'
string_sample2 = "first letteR is lowErcase"
string_sample3 = " extra whitespace string "
german_sample = "der Fluß"
some_string = "Hello"
count = 1
print(string_sample[0:4])
print(string_sample[-10:-5])
print(string_sample[5:])
print(string_sample[:10])
print(len(string_sample))

print('world' in string_sample)
print(some_string in 'Hello world')
print(some_string in 'Hello world', 'world' in 'Hello world')

print('Hello world'.lower())
print(string_sample.upper())

print(german_sample.lower())
print(german_sample.casefold())

print(string_sample2.capitalize())
print(string_sample2.capitalize().lower().upper())

print(string_sample2.strip('f'))

print(string_sample.replace('world', 'planet'))
print(string_sample[6:1])
print(type(string_sample[6:1]))
print(string_sample.replace('world', 'planet', 1))
print(string_sample.replace('world', 'planet', count))

print(string_sample.count('world', 0, 12))

# string_slice = string_sample[0:5]
# print(string_slice)
# print(type(string_slice))
# string_lower = string_sample.lower()
# print(string_lower)
# print(type(string_lower))

print(string_sample.find('world'))
found_index = string_sample.find('world')
print(string_sample[found_index:])
print(string_sample[6:])



# a = 'Hello'
# b = 'world'
# print(a, b)
# print(a + b)
# print(a + ' ' + b + '.' + str(123))

a = 'Your salary is'
b = 1000
new_string = a + ' ' + str(b)