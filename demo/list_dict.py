# person_list = ['Tyler', 39, True, False]

# person['admin'] = True
from pprint import pprint
# print(person)
# person['admin'] = False
# print(person['name'])
# print(person)
# person['age'] += 5
# print(person['age'])
person = {'name': 'Tyler', 'age': 39}
people = [ 
    {'name': 'Alden', 'age': 25},
    {'name': 'Adrian', 'age': 21},
    {'name': 'Katelyn', 'age': 20},
]

people[2]['name'] = "KC"

print(people[2]['name'])
pprint(people)
people.append(person)
pprint(people)