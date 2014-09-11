#!/usr/env/python

def aeng_greet():
	while True:
		import subprocess as s
		print('Welcome, Zachary')
		s.call('date')
		print('-'*30)
		print('    M A I N - M E N U')
		print('-'*30)
		print('1.Schematics')
		print('2.Item list')
		print('3.The Overseer')
		user_input = input('Enter your choice [1-3]: ')
		if user_input == 1:
			print ('1.Schematics')
		elif user_input == 2:
			s.call(['cat','items.txt'])
		elif user_input == 3:
			import cont_menu as cntrl
			cntrl.cntrl_Menu()
		elif user_input == str('q'):
			print ('Exiting..')
			break

