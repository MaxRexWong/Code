import random
up = ['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
symb = ['!','@','#','$','%','?']
psw = []
end = False

def gen(length):
    while length > 0:
        i = random.randint(1,5)
        if i == 1:
            psw.append(up[random.randint(0,25)])
        elif i == 2:
            psw.append(lower[random.randint(0,25)])
        elif i == 3:
            psw.append(symb[random.randint(0,5)])
        else:
            psw.append(random.randint(0,9))
        length -= 1

def getLength():
    length = int(input('Type the numeber of charaters your want in your password\n'))
    return length

def getPassword():
    gen(getLength())
    for elem in psw:
        print(elem,end='')

while end == False:
    getPassword()
    print()
    choice = input('Want another password? Type "yes" or "no"\n').lower()
    if choice == 'yes':
        psw = []
    elif choice == 'no':
        end = True
    else:
        print('Invaild input! Try again')