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
		noise()
	else:
		bear()
			
def noise():
	print("you hear a sound rising from behind.")
	answer = input("you either hide or not?")
	answer = answer.lower()
	if answer == "yes":
		print("you realize it is a car, drove by Mr. Mittag, out of the bush or not?")
		answerw = input()
		answerw = answerw.lower()
		if answerw == "yes":
			print("Mr. Mittag didn't notice you, and crush your leg, after you fully recovered, you miss the bus again.")
			hill()
		elif answerw == "no":
			print("the car drove away.")
			walk()
		else:
			print(answerw, "is not a good option, you need a better one.")
			noise()
	elif answer == "no":
		print("it is Mr. Mittag's SUV, he's happy to drive you to CFI.")
		drive()
	else:
		noise()

def walk():
	print("You need to keep walking, then you hear a hawl.")
	answer = input("You either run or not")
	answer = answer.lower()
	if answer == "yes":
		print("You twist your ankle by a rock, and tumble down 50 feet into ditch.")
		print(". \n. \n. ")
		print("Mr. Mittag rescue you after 2 hours, you fully recovered in 3 months")
		print(". \n. \n. ")
		print("You missed your bus to North Campus again!")
		print(". \n. \n. ")
		hill()
	elif answer == "no":
		print("the hawl dived to you and bite your ear down, Mr. Mittag hear your screaming, so he turn back and pick you up to hospital.")
		print(". \n. \n. ")
		print("After you out of hospital, you missed the CFI again")
		hill()
	else:
		walk()

def drive():
	print("Mr. Mittag's SUV tire has been punctured by a nail left by someone(abosuletly not Ryan)You guys need to push the car to North Campus.")
	print(". \n. \n. ")
	print("When you guys arrive, the CFI bus just drove back to main campus.")
	print(". \n. \n. ")
	tryagain()

def tryagain():
	print("try again?")
	answer = input()
	answer = answer.lower()
	if answer == "yes":
		intro()
	elif answer == "no":
		exit()
	else:
		tryagain()

i  =  1
while i == 1:
	intro()
