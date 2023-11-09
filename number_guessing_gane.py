import random

def game():
    num = random.randint(1,10)
    end = False
    count = 0
    print('Guess a number!')
    while end == False:
        count += 1
        ans = int(input())
        if ans < num:
            print('Too small!')
        elif ans > num:
            print('Too big!')
        else:
            print('Correct! You win')
            print(f'You have guess {count} times')
            end = True

play = True
print('Number guessing game')
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


