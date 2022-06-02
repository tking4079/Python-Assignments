"""
Name: Tegan
Date: 2 June 2022
asssignment 3

"""


#Ex3a: make a variable called alien_color and assign it a color
alien_color = 'green'

#Ex3b: write an if statement to test if the color is green. if it is, print 'player earned 5 points'
if alien_color == 'green':
    print('player earned 5 points')

#Ex3c: write one version of this test that passes the if test and another that fails
alien_color = 'yellow'
if alien_color == 'yellow':
    print('this program has passed')

if alien_color == 'red':
    print('this program has passed')

#Ex3d: using an if-else chain, if the alien color is green, print 'player earned 5 points for shooting the alien'
alien_color = 'green'
if alien_color == 'green':
    print('player earns 5 points for shooting the alien')
else:
    print('player earned 10 points')

#Ex3e: this version will print the else block since the statement is false
if alien_color == 'red':
    print('player earns 5 points for shooting the alien')
else:
    print('player earns 10 points')
