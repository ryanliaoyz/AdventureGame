
def intro():
     print('You need some deodorant you stink!')
     kitchen()
     
def kitchen():
	print('Your in the kitchen is it here?')
	ans = raw_input()
	ans = ans.lower()
	if ans=='yes':
		print('you idiot!!')
	elif ans=='no':
		print(" go left or right?") 
		direction=raw_input()
		direction=direction.lower()
		if direction=='left':
			bathroom()
		elif direction =='right':
			livingroom()
		else:
			kitchen()
	else:
		print("I don't understand you")
		kitchen() 
  
def bathroom():
	print('Your in the bathroom is it here?')
	ans = raw_input()
	ans=ans.lower()
	if ans=='yes':
		print('at least you know your deoderant should be')
		exit()
	elif ans=='no' or 'n':
		print(" go left or right?") 
		direction=raw_input()
		direction=direction.lower()
		if direction=='left':
			livingroom()
		elif direction =='right':
			kitchen()
		else:
			bathroom()
	else:
		print("I don't understand you")
		bathroom() 
   
def livingroom():
	print('Your in the livingroom is it here?')
	ans = raw_input()
	ans = ans.lower()
	if ans=='yes':
		print('weirdo!!')
	elif ans=='no':
		print(" go left or right?") 
		direction=raw_input()
		direction = direction.lower()
		if direction=='left':
			kitchen()
		elif direction =='right':
			bathroom()
		else:
			livingroom()
	else:
		print("I don't understand you") 
		livingroom()
   


while True:
	intro()
	print("Do you smell better now?")
	ans=raw_input()
	ans=ans.lower()
	if (ans=='no') or (ans=='n'):
		intro()
	else:
		print("Whatever ya wackjob!")
		exit()
