
#   Invert Hash
#   A hash table / hash map is an obj / dictionary
#   Given an object / dict,
#   return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys


dict1 = { 'name': 'Zaphod', 'charm': 'high', 'morals': 'dicey' }
expected1 = { 'Zaphod': 'name', 'high': 'charm', 'dicey': 'morals'}

dict2 = {'name': 'Adrian', 'age': 28}
expected2 = {'Adrian': 'name'}

def backwards(dictParam):
    new_dict = {}
    for i in dictParam.items():
        new_dict[i[1]] = i[0]
    print(new_dict)

backwards(dict1)
backwards(dict2)


