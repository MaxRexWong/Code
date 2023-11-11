import random

def gen():
    up = ['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    low = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
    symb = ['!','@','#','$','%','?']
    psw = []
    while True:
        try:
            length = int(input('How long should your password be? Type a number\n'))
        except ValueError:
            print('Invalid input')
            continue
        break
    while length > 0:
        i = random.randint(1,8)
        if i <= 3:
            psw.append(random.randint(0,9))
        elif i == 4 or i == 5:
            psw.append(up[random.randint(0,25)])
        elif i == 6 or i == 7:
            psw.append(low[random.randint(0,25)])
        else:
            psw.append(symb[random.randint(0,5)])
        length -= 1
    return psw

def main():
    while True:
        psw = gen()
        for elem in psw:
            print(elem,end='')
        print()
        while True:
             choice = input("Want another password?(yes/no)\n").lower()
             if choice in ['yes', 'no']:
                 break
             else:
                 print('Invalid input')
        if choice == 'no':
            print('Bye!')
            break

main()
