prices = {  'banana' : 4, 
            'apple' : 2 , 
            'orange' : 1.5 ,
            'pear' : 3
}

############ Create another dictionary called stock ###########

stock = {  'banana' : 6, 
            'apple' : 0 , 
            'orange' : 32 ,
            'pear' : 15
}

############ Loop through each key in prices ###########

for k , v in prices.items():
    print(k)
    print('price: ',prices[k])
    print('stock: ',stock[k])

############ Sold all of your food ###########

total = 0

for k in prices:
    total = total + prices[k] * stock[k]

print('You can earn total',total,'$')