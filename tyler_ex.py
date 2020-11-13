#.py file that does the same thing as the web project, but in command prompt

import os
import time

object_dictionary = {
	'object_one':True,
	'object_two':True,
	'object_three':True,
	'object_four':True,
	'object_five':True,
}

values = [value for value in object_dictionary.values()]
keys = [key for key in object_dictionary.keys()]

print(values,'\n')

def collision(which_object):

	which_object = 'object_{}'.format(which_object)
	print()

	if which_object in keys:

		print("You hit something!")

		object_dictionary[which_object] = False

		values = [value for value in object_dictionary.values()]
		
		print(values,'\n')

		if all([x == False for x in object_dictionary.values()]):

			for x in range(3,0,-1):
				os.system('clear')
				print("They're all dead!!\n")
				print("Now I'm going to reset the game in {}".format(str(x)))
				time.sleep(1)

			for key in keys:
				object_dictionary[key] = True

		else:
			pause = input("They're not all dead yet, hit enter to keep going!")

		os.system('clear')

	else:

		print("Doesn't seem like that matches an object. Make sure you're typing out 'one, two, three, etc.'\n")

		values = [value for value in object_dictionary.values()]
		
		print(values,'\n')
		pause = input("Let's try that again! Hit enter to continue")
		os.system('clear')

while True:

	which_object = input('Type out the number of the object you have collided with (one through five): ')

	collision(which_object)


# Okay so this game is a little more straightforward than the js file and hopefully easier to follow if you're stuck
# Same basic principal, the game initializes with a series of objects and their states. This time I used a dictionary because it's a little cleaner. A dictionary has {key:value} as a format.
# You can call a specific value by calling that value's key.

# In this case, I establish the dictionary object itself, along with two arrays containing the values and the keys inside that dictionary object
# The code is on an infinite cycle in a while True: loop. Each iteration establishes an event (in this case by you manually typing it out, see line 62 "which_object = input(...)"). 
# It then passes the name of the object involved in that event into a function called collision (line 64)

# This function will check the name of the object against the dictionary that we created containing the objects we care about. (Line 24 "if which_object in keys:")
# If the object is one we care about, then it uses line 28 "object_dictionaries[which_object]" to index the appropriate object and change its value to False

# Then it prints some stuff out for legibility and on line 34 it checks all the items in the dictionary's value list to see if they're all False. If they are, the first loop on line 36 is just for aesthetics.
# The loop on line 42 will iterate over each key in object_dictionary, and assign True for each key-value pair. Thereby 'resetting' the game

# If line 34 shows that all the objects have NOT been collided with, and there is a 'True' or 'Alive' value in there, then the game continues through the else statement on line 45

# The else on line 50 is just to make sure that if you type something completely left-field the program just asks you for an input again. This is because when you type something like "baseball", the program will format
# that string via line 21 to be "object_baseball" which is not a key value in the dictionary. Even if you type "1" the string will just be "object_1" which is again, not a key in the dictionary.
# I could have added more logic or a better interface but this script was slightly more rushed than the other one.

# Hope this helps brudda!!