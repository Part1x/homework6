my_dict = {'Denis':1999, 'Max':2000,'Petr':1998}
print('Dict:', my_dict)
print('Existing value:', my_dict['Max'])
print('Not existing value:',  my_dict.get('Anton'))
my_dict.update({'Sergey': 2000,'Sasha': 1999})
a = my_dict.pop('Max')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

my_set = {1, 2, 1, 2, 3, True, 'Snow', 'Ball', 'Snow'}
print('Set:', my_set)
my_set.update([5, 'White'])
my_set.discard('Snow')
print('Modified set:', my_set)