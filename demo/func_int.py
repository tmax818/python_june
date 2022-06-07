


# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
# print(x[1][0])
# print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
# print(students[0]['last_name'])
# print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'][0])
# print(sports_directory)
# Change the value 20 in z to 30

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
# print(z[0]['y'])
# print(z)


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(listParam):
    for student in listParam:
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")


# iterateDictionary(students)
# iterateDictionary([{'name': 'Tyler', 'age': 39}])
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# my_list = [0,1,2,3,4,5]

# for i in my_list:
#     print(i)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(param):
    print(len(param['locations']), 'LOCATIONS')
    for location in param['locations']:
        print(location)
    print()
    print(len(param['instructors']), 'INSTRUCTORS')
    for instructor in param['instructors']:
        print(instructor)


printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
