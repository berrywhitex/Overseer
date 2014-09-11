def src_menu():
	import subprocess as sub
	print('-'*30)
	print('    S O U R C E')
	print('-'*30)
	print('1.Main')
	print('2.Packages')
	print('-'*30)
	user_input = input('Enter your choice [1-2]: ')
	if user_input == 1:
		sub.call(['cat','main.py'])
	elif user_input == 2:
 		print('-'*30)
		print('    S O U R C E')
		print('-'*30)
		print('1.authpage.py')
		print('2.')
		print('-'*30)
		
