item = ['T-Shirt','Sweater']
while True:
    request = input('Welcome to our shop, what do you want (C, R, U, D)? : ')
    request = request.upper()
    if request == 'R':
        print('Our items: ',item)
    elif request == 'C':
        new_item = input('Enter new item: ')
        item.append(new_item)
        print('Our items: ',item)
    elif request == 'U':
        new_position = int(input('Update position?: '))
        new_item = input('Enter new item: ')
        item[new_position - 1] = new_item
        print('Our items: ',item)
    elif request == 'D':
        del_pos = int(input('Delete position?: '))
        del item[del_pos - 1]
        print('Our items: ',item)
    else:
        print('Unknow request, try again?: ')