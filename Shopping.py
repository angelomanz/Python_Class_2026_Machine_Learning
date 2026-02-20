items = ['apples', 'bread', 'milk']

items.append('eggs')
items.append('cheese')
items.remove('bread')
items.insert(0, 'butter')

print('Shopping list:', items)
print('Total items:' , len(items))
print('Frist item:' , items[0])
print('last item:' , items[-1])