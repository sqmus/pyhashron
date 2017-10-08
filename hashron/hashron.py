#!/usr/bin/python


from __future__ import division
import os
import sys
import hashlib
import datetime

__doc__ = ("""hashron module - Hash testing and fetching using hashlib module


basicly hashron goals if guess infromation from hash, what the
information before hash using generated and fetch all posibility
from input keyword and predicted length

How i use this ?
----------------

is tool for testing and fetching hash
with generated char inputed in keyword.
the goal is guess information from hash.


	from hashron import *

Import hashron to you script


	# hashron.begin(<str>,<int>,<str>)
	hashron.begin('<Keyword String>',<Long key predict>,'<Target Hash>')

these function will try all posibility as 
long <Long key predict> char from <Keyword String>
and hashed to fetching with <Target Hash> hash.


	#hashron.benchmark(<str>)
	hashron.benchmark(<keyword>)


these function for test average hash processing 
time on your machine.

Installation
------------


    $ pip install hashron


Resources
---------

GitHub repository <https://github.com/sqmus/pyhashron>
""")

def benchmark(listkey):
	start = datetime.datetime.now()  # variable for put time start of benchmarks
	hashlib.md5(listkey).hexdigest() # hashing listkey using md5
	hashlib.sha1(listkey).hexdigest() # hashing listkey using sha1
	hashlib.sha224(listkey).hexdigest() # hashing listkey using sha244
	hashlib.sha256(listkey).hexdigest() # hashing listkey using sha256
	hashlib.sha384(listkey).hexdigest() # hashing listkey using sha384
	hashlib.sha512(listkey).hexdigest() # hashing listkey using sha512
	# if there a unavailable hash metode you can add here the
	# code of hashing function of the new algotirhm
	end =  datetime.datetime.now() # variable for put time end of benchmarks
	clock = end - start # creatinf time delta for precision time
	return (clock.total_seconds()/(32+40+64+94+128)) # time devide by whole hash length
		
def begin(listkey,longkey,thash):
	found = False # define found or not
	counter =0 # define counter progress
	if os.name == 'nt':
		clear = 'cls'
	else:
		clear = 'clear'
	setsample = len(listkey)**longkey # Calculate cardinal of sample space
	print "[!]Probability " + str(1/setsample) + "from " + str(setsample) # Calculate Probability of Posible
	print "[ ]Detecting Hash type.." 
	if (len(thash) == 32): # Predict hash from it target length
		hashtype = 'md5' # Define hashtype based on target hash length
	elif (len(thash) == 40):
		hashtype = 'sha1'
	elif (len(thash) == 56):
		hashtype = 'sha224'
	elif (len(thash) == 64):
		hashtype = 'sha256'
	elif (len(thash) == 96):
		hashtype = 'sha384'
	elif (len(thash) == 128):
		hashtype = 'sha512'
	else:
		hashtype = raw_input("[*]Input Hash Type")# function for special implemnted hashing functions
	print "\t[*]" + hashtype
	print "[!]Predicting elapsed time : " + str(((benchmark(listkey)) * (setsample))) + " s\n\n" #benchmarking time multiplied by size of setsample
	sttime = datetime.datetime.now()
	for current in xrange(longkey): #Iteration for many key length generated
		arbitrary_chr = [i for i in listkey]
		for y in xrange(current): # Iteration for generated char
			arbitrary_chr = [x+i for i in listkey for x in arbitrary_chr] # storing the generated char
		for ar in arbitrary_chr:
			counter+=1
			print ("[ "+str(counter) + " / " + str(setsample) +" ( " + str(float(counter/setsample)*100) +"% )]")
			endst = datetime.datetime.now()
			print "[*] Time elapsed " + str(endst - sttime) # Calculate time elapse
			if (hashtype == 'md5'): # kind of hash type
				if (hashlib.md5(ar.encode()).hexdigest() == ''+thash): # Compare str hash generated char with target hash was inputed
					print "[*] " + thash + " ( "+ hashtype.upper() +" )as " + ar # showing the result of exact hash
					found = True # Parameter of found
					quit() # exit program mean the progess has done
				else:
					os.system(clear) # clear screen
			elif (hashtype == 'sha1'):
				if (hashlib.sha1(ar.encode()).hexdigest() == thash):
					print "[*] " + thash + " ( "+ hashtype.upper() +" )as " + ar
					found = True 
					quit()
				else:
					os.system(clear)
			elif (hashtype == 'sha224'):
				if (hashlib.sha224(ar.encode()).hexdigest() == thash):
					print "[*] " + thash + " ( "+ hashtype.upper() +" )as " + ar
					found = True
					quit()
				else:
					os.system(clear)
			elif (hashtype == 'sha256'):
				if (hashlib.sha256(ar.encode()).hexdigest() == thash):
					print "[*] " + thash + " ( "+ hashtype.upper() +" )as " + ar
					found = True 
					quit()
				else:
					os.system(clear)
			elif (hashtype == 'sha384'):
				if (hashlib.sha384(ar.encode()).hexdigest() == thash):
					print "[*] " + thash + " ( "+ hashtype.upper() +" )as " + ar
					found = True 
					quit()
				else:
					os.system(clear)
			elif (hashtype == 'sha512'):
				if (hashlib.sha512(ar.encode()).hexdigest() == thash):
					#os.system(clear)
					print "[*] " + thash + " ( "+ hashtype.upper() +" )as " + ar
					found = True 
					quit()
				else:
					os.system(clear)
			# if there not implemented algorithm / new algorithm you can put code with template
			# [ELIF/IF](hashtype <-- <nama hashtype>):
			# 	if hashlib.<new algorithm>(<parameter of algorithm need>).hexdigest() == thash: # founded hash
			# 		print <-- results
			#  		found <-- boolean for found exact hash fetch
			# 		quit <-- for finishing program
			#   else:
			#		[clear screen]
			# [ELSE]		
			else:
					print "[*]Not Found"
		if ~(found):
			print "[*] Not Found"
