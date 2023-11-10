import random

def game():
    num = random.randint(1,10)
    end = False
    count = 0
    print('Guess a number from 1 to 9')
    while end == False:
        check = False
        count += 1
        if count == 5:
            print('You loss')
            break
        ans = str(input())
        while check == False:
            if ans=='1'or ans=='2'or ans=='3'or ans=='4'or ans=='5'or ans=='6'or ans=='7'or ans=='8'or ans=='9':
                ans = int(ans)
                check = True
            else:
                print('Out of range! Enter again')
                ans = str(input())
        if ans < num:
            print('Too small!')
        elif ans > num:
            print('Too big!')
        else:
            print('Correct! You win')
            print(f'You have guess {count} times')
            end = True

play = True
print('Number guessing game. You can guess 4 times')
game()
print('Wanna play again?')
while play == True:
    choice = input('Type "yes" or "no\n').lower()
    if choice == 'yes':
        game()
    elif choice == 'no':
        print('See you later than')
        play = False
    else:
        print('Invalid input! Try again')

