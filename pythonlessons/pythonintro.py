#session1 29/09
print("hello world")
print('5+4')
print(5+4)
personName= 'Edward' #string
personHeight= '6.1'#float
personAge = '28'#integer
programmingFun = True #boolean

print(personName,personAge,personHeight,programmingFun)

#casting
personHeight = int(6.8) #converted float to int
print(personHeight)

#string
fact1 = 'Svalbard Vault'
fact2 = 'Norway'

#string concatenation
print(fact1 + ' ' + fact2)

#string formatting
#placeholder in curly braces
print(f'{fact1} is an interesting facility to visit. It is in {fact2}.')

#indexing - first letter of the string
print(fact1[0])
print(fact1[-1]) #negative index starts at theend

print(len(fact1)) #length function

#string slicing
print(fact1[0:3]) #[start index:end index] last index is not included in output
print(fact1[:3]) #starts at 0. if you don't mention the end it will go to the end
print(fact1[:]) #prints everything

#if else
if 10>20:
    #indentation added after all colons. only one block runs if multiple true and its the top one in the order first come first server 
    print('the if condition is true')
    print('second line in the if block')
elif 'cat'=='cat': #= is assign, == is equality
    print('cat has got night vision')
else:
    print('none of the conditions are true')

#match
luckynumber = 7
match luckynumber:
    case 1:
        print('1 is your lucky number')
    case 2:
        print('2 is your lucky number')
    case 7:
        print('7 is your lucky number')
    case _:
        print('none of the cases match')

    