#!/usr/bin/python
#Menu for engine controls#
def cntrl_Menu():
	print('-' * 30)
	print('   T H E - O V E R S E E R ')
	print('-' * 30)
	print('1. Camera (PoV)')
	print('2. Camera (down)')
	print('3. Flight Data')
	choice = input('Enter your choice [1-3]: ')
	##Recieves input, and uses 

	if choice == 1:
		print ('POV CAM')
		cntrl_Menu()
							
	elif choice == 2:					
		print ('BOTTOM CAM')
		cntrl_Menu()
				
	elif choice == 3:
				
		print('FLIGHT DATA')
		cntrl_Menu()
#	elif choice == 'q':
#		print('Exiting..')

	else:
		print('That is not an option.')
		cntrl_Menu()		

if __name__ == "__main__":
	cntrl_Menu()	
