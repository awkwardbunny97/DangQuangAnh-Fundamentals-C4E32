def get_even_list(l):
    enum = []
    for i in l:
        if i % 2 == 0:
            enum.append(i)
    return enum

print(get_even_list([1,4,5,-1,10]))