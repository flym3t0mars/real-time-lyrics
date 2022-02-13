#! /bin/python
import os,sys,time

def clear():
	try:
		os.system('clear')
	except:
		os.system('cls')
	else:
		pass
	return

def lyrics():
	global s
	s=''

def main():
	clear()

if __name__=="__main__":
	main()

