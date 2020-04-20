names = ['Kajal', 'Pundrik', 'Vrinda', 'Neha']


# for name in names:
#     # print('Hello there, '+ name)
#     print(', '.join(['Hello there', name, 'PM']))


print(names)
print(', '.join(names))


# import os
# location_of_files = 'C:\\Users\\hp\\Desktop\\Codearray\\IntermediatePythonProgramming'
# file_name = 'example.txt'
# print(location_of_files+ '\\'+ file_name)
# with open(os.path.join(location_of_files,file_name)) as f:
#     print(f.read())

who = 'Pundrik'
how_many = 12
# Pundrik bought 12 apples today!
print(who, 'bought', how_many, 'apples today!')
# print(who+ 'bought' + how_many+ 'apples today!')
print('{} bought {} apples today!'.format(who,how_many))
print('{0} bought {1} apples today!'.format(who,how_many))
print('{1} bought {0} apples today!'.format(who,how_many))

