#1/10/2025
petName = 'Cat'
match petName:
    case 'Panda':
        print('Pandas eat fo 14 hours a day.')
    case 'Dog':
        print('Dog has got a good sense of smell')
    case _:
        print('None of the cases match.')

#Loops: execute a block of code as long as the condition is true
#1. WHILE loop, components: a. initialisation, b. condition, c. increment
w = 0 #a. initialisation
while w < 10: #b. condition
    print(w)
    w = w + 1 #c. increment
#break 
i = 1 
while i < 10:
    print(i)
    if i == 3:
        break
    i = i + 1

#continue
w = 0
while w < 10:
    w = w + 1
    if w == 3:
        continue
    print(w)

#2. FOR loop, components: a. temporary variable, b. container
gemList = ['Ruby', 'Diamond', 'Pearl']
#   a.         b.
for Edward in gemList:
    pass #need to 'reserve' indentation
print

for Edward in gemList:
    print(Edward)
    if Edward == 'Diamond':
        break

for x in 'dragon fruit':
    print(x)

for x in range(2,50,5): #range(start,end,step) starts at 0 if not specified, step = 1 range is a container
    print(x)

#Data Collection
#1. List, 2. Tuple, 3. Set, 4. Dictionary  list allows dupes, set doesn't
#properties
#list, properties - ordered, changeable, allow duplicates
sportsList = ['tennis','cricket','hockey','football']
print(sportsList)
print(len(sportsList))
sportsList[1] = 'ice hockey' #overrides index 1
print(sportsList)

#insert
sportsList.insert(1, 'table tennis')
print(sportsList)

#append add to end oflist - doesn't need index
sportsList.append('orange')
print(sportsList)

#extendto add 2 lists todether
gemList.extend(sportsList)
print(gemList)

#remove to remove a value
sportsList.remove('tennis')
print(sportsList)

#pop to remove an index
sportsList.pop(2)
print(sportsList)

#sportsList.pop()removes the last index


#2. tuple, properties - ordered, unchangeable, allow duplicates
myTuple = ('astrobiology','scuba diver', 'rr liner')
print(myTuple)

#convert tuple to list and then back to tuple to edit
myTupleList = list(myTuple)
myTupleList[1] = 'engineer'
updatedTuple = tuple(myTupleList)
print(updatedTuple)
#3. set, properties - opposite to list - unordered, unchangeable, no duplicates
mySet={'range rover', 'toyota', 'peugeot','vauxhall'}
print(mySet)

#4. dictionary: properties - ordered, changeable, no duplicates
myDictionary = {
    'brand':'ford', 
    'model':'mustang',
    'year' : 2023,
    'year' : 2022,
    }
print(myDictionary)
print(myDictionary.keys())
print(myDictionary.values())

#functions or methods - a block of code that runs only when you call it
#camelCase for variable - 1st small, 2nd capital. For functions PascalCase, 
#compiler doesn't run fn, it skips fn then reads the function call then runs the function when its called
def MyFunction():
    print('MyFunction runs')
    print('sugar cane is a grass.')

#function call
MyFunction()

#parameters and arguments

def PersonInfo(personName,personJob,personCountry): #variable/parameters
    print(personName,personJob,personCountry)

PersonInfo('Edward','CyberSecurity','London')#values/arguments

#default argument
def MyCountry(countryName='UK'):
    print('I am from ' + countryName)
MyCountry()

#return value
def MyMath(x):
    return x+3
print(MyMath(10))
