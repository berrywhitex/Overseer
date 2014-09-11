#/usr/env/python

def seng_greet():
	import subprocess as s
	print('Welcome, Michael.')
	s.call('date')
	#Menu#
	print('-' * 30)
	print('	M A I N - M E N U')
	print('-' * 30)
	print('1.Source')
	print('2.Item list')
	print('3.The Overseer')
	print('-' * 30)
	#Recieve user input#
	user_input = input('Enter your choice [1-3]: ')
	#Checks input and runs accordingly#
	import source as src
	if user_input == 1: 	
		src.source()
	elif user_input == 2:
		s.call(['cat','items.txt'])
	elif user_input == 3:
		import cont_menu as cntrl
		cntrl.cntrl_Menu()
	elif user_input == int('q'):
		print('Exiting..')
		
	else:
		print('THAT IS NOT AN OPTION!')
		seng_greet()

seng_greet()
