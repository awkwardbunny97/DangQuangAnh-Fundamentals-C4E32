def is_inside(array1,array2):
    # array1 = ['x','y']
    # array2 = ['a','b','h','w']
    if array1[0] in range(array2[0],array2[2] + array2[0] + 1) \
    and array1[1] in range(array2[1],array2[3] + array2[1] + 1):
        return True
    else:
        return False

print(is_inside([200 , 120],[140 , 60,  100 , 200]))
