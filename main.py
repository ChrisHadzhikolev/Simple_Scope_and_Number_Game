import random as rand

number = rand.randint(1, 100)
print('I am thinking of a number between 1 and 100...')
mode = input('Enter e for easy and h for hard: ').lower().strip()
attempts = 0
if mode == 'e':
    print('You have 10 attempts')
    attempts = 10
elif mode == 'h':
    attempts = 5

success = False

while attempts > 0 and not success:
    guess = int(input('Your guess: '))
    if guess == number:
        print(f'Congrats you guessed the number {number} with {attempts} attempts left!')
        success = True
    elif guess > number:
        print('Too High')
        attempts -= 1
        print(f'You have {attempts} left')
    elif guess < number:
        print('Too Low')
        attempts -= 1
        print(f'You have {attempts} left')

if not success:
    print('You ran out of attempts')
