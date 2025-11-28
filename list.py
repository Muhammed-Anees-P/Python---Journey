#
#List
#List is a collection of different data types, it is ordered and changeable(mutable)
list = ['anees','muhammed', 'p', 'anees']

#
print(list)
print(type(list))

#allow duplicate
print(len(list))

#access item
print(list[1])
print(list[-1])
print(list[0:3])

#change item

list[1] = 'car'
print(list)


print('============================================================')


vehicle = ['car', 'bus', 'lorry']
vehicle.append('bike')
print(vehicle)

print(len(vehicle))

vehicle.insert(1,'truck')
print('insert item on 1st index',vehicle)

print(len(vehicle))

vehicle.remove('lorry')
print('remove item lorry only',vehicle)

print(len(vehicle))

#pop method remove last item

vehicle.pop()
print('remove last item',vehicle)

print(len(vehicle))

del vehicle[0]
print('delete first item',vehicle)

print(len(vehicle))

vehicle.clear()
print('clear list',vehicle)


print('============================================================================')