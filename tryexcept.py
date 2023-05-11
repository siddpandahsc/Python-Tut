try:
    x = int(input('Enter an int: '))
    print(x)
except ValueError:
    print('Value not an int'+name)
# else:
#     print('Nothng went wrong')
finally:
    print('try except finished')