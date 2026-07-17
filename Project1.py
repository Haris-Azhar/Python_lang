# Creating Snake,Water,Gun game
'''
1 for water
2 for snake
0 for gun
'''
import random
computer = random.choice([1,2,0])
your_choice = input('Enter a choice : ')
yourDict = {
    's' : 2,
    'w' : 1,
    'g' : 0
}
reversedict = {
    2 : 'Snake',
    1 : 'Water',
    0 : 'Gun'
}
you = yourDict[your_choice]

# By  showing choice of computer and you
print(f'Computer chose {reversedict[computer]} \n You chose {reversedict[you]}')

if computer == 1 and you ==1:
    print('its draww')
else:
    if computer == 1 and you ==2:
        print('You win!')
    elif  computer == 1 and you == 0:
        print('You losee!')
    elif computer == 2 and you == 1:
        print('You losee!')
    elif computer == 2 and you == 0:
        print('You win!')
    elif computer == 0 and you == 1:
        print('You win!')
    elif computer == 0 and you == 2:
        print('You losee!')
    else:
        print ('Something went wronge')

