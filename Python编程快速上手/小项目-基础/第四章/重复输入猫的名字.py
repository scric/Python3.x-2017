def repeatInput():
    catName = []
    while True:
        print('Enter the name of cat ' + str(len(catName) + 1) + ' ( Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        catName += [name]
    print('The cat names are:')
    return catName


catNames = repeatInput()

for i in catNames:
    print('  ' + i)