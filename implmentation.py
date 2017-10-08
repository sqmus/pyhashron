#!/bin/python
#	Copyright (C) 2017  sqmus
#
#	This program is free software; you can redistribute it and/or
#	modify it under the terms of the GNU General Public License
#	as published by the Free Software Foundation; either version 2
#	of the License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program; if not, write to the Free Software
#	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# This Hashron module with build implemented function .
from hashron import *

try:
        print ("""
              _   _           _                     
  _ __  _   _| | | | __ _ ___| |__  _ __ ___  _ __  
 | '_ \| | | | |_| |/ _` / __| '_ \| '__/ _ \| '_ \ 
 | |_) | |_| |  _  | (_| \__ \ | | | | | (_) | | | |
 | .__/ \__, |_| |_|\__,_|___/_| |_|_|  \___/|_| |_|
 |_|    |___/
 
 Hash Brutoforce Module ( MD5, SHA1, SHA-224, SHA-256, SHA-384, SHA-512 Available)
 Implementation Hashron on python script, github.com/sqmus/pyhashron
 Licenses under GNU GPLv2
 """)
        if(sys.argv[2] > 0 and sys.argv[2] != sys.argv[2] < 0): # check for making positive integer
        	print("[*] Long Key should positive integer")
        core.begin(sys.argv[1],int(sys.argv[2]),sys.argv[3])
except IndexError:
		print (" " + sys.argv[0] +" <Keyword A..Z> <Long Key 1..integer> <Target Hash>")
		exit(1)
