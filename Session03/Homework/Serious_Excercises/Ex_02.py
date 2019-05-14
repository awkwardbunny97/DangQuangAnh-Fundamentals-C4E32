list_sheep = []
############## Enter Sheep Size #############
while True:
    request =  int(input('Enter your sheep size: '))
    if request == 0:
        print('Hello, my name is Quang Anh and these are my sheep size: ',list_sheep)
        break
    else:
        list_sheep.append(request)
        print('Hello, my name is Quang Anh and these are my sheep size: ',list_sheep)

############## Finding biggest one #############

print('Now my biggest sheep has size',max(list_sheep),"let's shear it")


############## After shearing #############

# list_sheep [list_sheep.index(max(list_sheep))] = 8
# print('After shearing, here is my flock',list_sheep)

############## After 4 months #############

for i in range(4):
    print('Month', i + 1)
    for v in range(len(list_sheep)):
        list_sheep[v] = list_sheep[v] + 50
    print('1 month has passed, now here is my flock',list_sheep)
    list_sheep [list_sheep.index(max(list_sheep))] = 8
    print('After shearing, here is my flock',list_sheep)

############## Selling #############

print('My flock has size in total: ',sum(list_sheep))  
print('I would get',sum(list_sheep),'* 2$ =',sum(list_sheep)*2,'$') 

############## End program #############