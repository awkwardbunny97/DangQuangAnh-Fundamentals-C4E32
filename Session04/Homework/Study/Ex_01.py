alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
raw_string = input('Input your string: ')
raw_string = raw_string.lower()
count_alphabet = {}

for i in range(len(alphabet)):
    if  (raw_string).count(alphabet[i]) != 0:
        count_alphabet[alphabet[i]] = (raw_string).count(alphabet[i])

for k,l in count_alphabet.items():
    print(k," ",l)