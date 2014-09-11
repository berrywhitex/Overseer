#!/usr/bin/python

def auth_proc():
	user_input = raw_input("Name: ")
	password = raw_input("Password: ")
	if user_input == 'Michael Owens Jr':
		if password == ("stalio").lower:
			import seng
			seng.sEng()
	elif user_input == "Zachary Owens":	
		if password == ("stalio").lower:	
			import aeng
			aeng.aEng()

if __name__ == "__main__":
	import subprocess as sub
	sub.call('clear')
	auth_proc()
