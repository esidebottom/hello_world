for x in range(1,5):
    if x%5 == x%3 == 0:
        print('fizzbuzz')
        continue
    if x%3 == 0:
        print('fizz')
        continue
    if x%5 == 0:
        print('buzz')
        continue
    print(x)