#/usr/bin/env python

import ftplib

f = open('FTPList.txt')
lines = f.readlines()

output = open('openFTP.txt', 'w')

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'me@your.com')
		print '\n[*] ' + str(hostname) +\
		'FTP Anonymous Logon Succeeded.'
		ftp.quit()
		output.write(str(hostname) + "\n")
	except Exception, e:
		print '\n[-]' + str(hostname) +\
		'FTP Anonymous Logon Failed.'