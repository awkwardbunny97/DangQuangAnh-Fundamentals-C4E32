inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

###### Add a key to inventory called 'pocket' ###

inventory['pocket'] = ['seashall' , 'strange berry', 'lint']

###### Remove 'dagger' from the list ###

inventory['backpack'].remove('dagger')

###### Add 50 to the number stored under the 'gold' key ###

inventory['gold'] = inventory['gold'] + 50

###### Result ###

print(inventory)