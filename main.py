def intro():
	print("You are a freshman in South Kent School, you missed the lunch and about miss the CFI in North Campus!")
	hill()

def hill():
	print("The bus to CFI just departure!")
	answer = input("Chase or not?")
	answer = answer.lower()
	if answer == "yes":
		halfway()
	elif answer == "no":
		dorm()
	else:
		hill()

def halfway():
	print("you runs half way down the mountain, driver doesn't see you(or pretend)")
	answer = input("Continue or not?")
	answer = answer.lower()
	if answer == "yes":
		print("you crashed by the car when chasing, you fully recovered after 6 month, and you missed the bus to CFI again!")
		hill()
	elif answer == "no":
		dorm()
	else:
		halfway()

def dorm():
	print("You go back to dorm, You friend told you if you miss the CFI you will be knocked out from South Kent.")
	answer = input("stay in dorm or not?")
	answer = answer.lower()
	if answer == "yes":
		print("Mr. Darrin have a conversation with you, you could remain in school but can’t have any class absence. Sadly, you missed the bus to CFI again.")
		hill()		
	elif answer == "no":
		figure()
	else:
		dorm()

def figure():
	print("You find out there’s only two ways to reach CFI, Hero’s journey pass(on foot) or Uber.")	
	answer = input("Walk or not?")
	answer = answer.lower()
	if answer == "yes":
		bear()
	elif answer == "no":
		print("you open the Uber app, it shows “no cars available”")
		figure()
	else:
		figure()

def bear():
	print("you start walking, and out of nowhere a bear appears. You either fight it or run.")
	answer = input("fight or not?")
	answer = answer.lower()
	if answer == "yes":
		print("What weapon do you wanna use.")
		answerw = input("stick or stone?")
		answerw = answerw.lower()
		if answerw == "stick" or answerw == "stone":
			print("you wounded, by the dumb decision of fighting with a bear with a ", answerw, " and you fully recovered after 6 month, and you missed the bus to CFI again.")
			hill()
		else:
			print("how could you have a ", answerw,"in mid of the forest?")
			bear()
	elif answer == "no":
		print("The bear doesn’t chase you, you make alive safely from the bear.")
		exit()
	else:
		bear()
			


i  =  1
while i == 1:
	intro()
