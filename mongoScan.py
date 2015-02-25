#/usr/bin/env python

import pymongo

f = open('mongoList.txt')
lines = f.readlines()

output = open('openBD.txt', 'w')

for line in lines:
	try:
		client = pymongo.MongoClient(line,27017) #27017
		print "Connected successfully!!! to " + str(line)
		output.write(line)
		
		try:
			dbs = client.database_names()
			output.write(str(dbs) + "\n")
			print client.database_names()
		except:
			print "not authorized on admin to execute command"

	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
		print "Failed: %s" % line