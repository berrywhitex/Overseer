#!/usr/env/python

def pkg_menu():
	import subprocess as s
	print('-'*30)
	print('    P A C K A G E S')
	print('-'*30)
	print('1. authpage.py')
	print('2. cont_menu.py')
	print('-'*30)
	b = input('Enter your choice [1-4]: ')
	if b == 1:
		s.call(['cat','authpage.py'])
		pkg_menu()
	elif b == 2:
		s.call(['cat','cont_menu.py'])

	else:
		print('THAT IS NOT AN OPTION!')

