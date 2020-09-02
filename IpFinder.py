import os,pyfiglet

print(pyfiglet.figlet_format("IPfinder",font="slant"))
print('\033[93m' +"[*] IP adress is getting...")

ip =os.popen("curl https://httpbin.org/ip -s | sed '2!d' | grep -oP '(:).*'")
ip = ip.read()
saveip = ip[2:]
print('\033[32m' + f"[+] Your IP adress{ip}" + "\033[0m ")

while True:
	save = input("Do you want to save your IP address ?(Y/N)")
	if save == "Y" or save == "y":
		with open("IP_adresses","a",encoding="UTF-8") as file:
			file.write(saveip + "\n")

		print('\033[32m' + "[+]Saved : " + os.getcwd() + "/IP_adresses.txt" + "\033[0m ")
		break
	elif save == "N" or save == "n":
		break
	else:
		print('\033[31m' + "[-]Invalid Input" + "\033[0m ")
