from random import randint
import sys
print()
print("Hi! Let's play a <Guess a number> game. To quit the game, write 'exit'")
c = 0
while True:
    a = input('Choose a range of numbers to deal with (for example "1-100"):\n')
    if a == 'exit':
        print('It was fun!')
        sys.exit()
    try:
        a = list(map(int,a.split('-')))
        if len(a) != 2:
            raise ValueError
    except ValueError:
        print('Please, choose right values')
        continue
    num = randint(min(a),max(a))
    while True:
        attempt = input('Try to guess the number:\n')
        if attempt == 'exit':
            print('It was fun!')
            sys.exit()
        try:
            attempt = int(attempt)
        except ValueError:
            print('Please, choose the right value')
            continue
        c += 1
        if attempt == num:
            print(f"You've won! Amount of attemts - {c}")
            c = 0
            break
        print("Miss! Try again")