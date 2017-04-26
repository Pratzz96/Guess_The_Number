#! /usr/bin/env python3
import random
guessesTaken = 0
print('_________________________________Welcome To Guess the Number Game_______________________________________________________\n')
print('Hello! What is your name?')
myName = input()
#Use the input function for Take the input as a string of character or numbers as given by user according to the user name 
number = random.randint(1, 20)
#Use the random function to generate a number between 1 to 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
#Use a while loop to take the number input, only 6 time guess is allow for user who want to play this game if you want to extend the guess limit change the limit of guessTaken more than or less than 6 as you want also in while loop comparison is also happen between the random numnber generator by the random function and enter by the user.
while guessesTaken < 6:
	print('Take a guess.')
	guess = input()
	guess = int(guess)
	guessesTaken = guessesTaken + 1
	if guess < number:
		print('Your guess is too low.')
	if guess > number:
		print('Your guess is too high.')
	if guess == number:
		break
if guess == number:
	guessesTaken = str(guessesTaken)
	print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
	number = str(number)
	print('Nope. The number I was thinking of was ' + number)
