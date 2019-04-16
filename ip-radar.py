#!/usr/bin/env python3

#
# --------------------------------------------------------------------------------------------------
#  ip-radar.py:
#  Checks geolocations of ips in a list file.
#
#  This is the official list of the authors and copyright owners.
#  Copyright (C) 2019 - Adam Lee
#  Name/Organization <email address>
#  @author Adam Lee
# --------------------------------------------------------------------------------------------------
#

# Python native library includes
import os
import re
import subprocess
import json
from termcolor import colored
import urllib.request
import urllib.parse

class ipRadar:
	@staticmethod
	def print_app_name():
		format_text = \
		'''                                                                                
		    _                            __          
		   (_)___        _________ _____/ /___ ______
		  / / __ \______/ ___/ __ `/ __  / __ `/ ___/
		 / / /_/ /_____/ /  / /_/ / /_/ / /_/ / /    
		/_/ .___/     /_/   \__,_/\__,_/\__,_/_/     
		 /_/                                         
		 '''
		print(colored(format_text, 'green', attrs=['blink']))
		print()


def FileOpen(fn) -> str:
	if fn:
		try:
			f = open(fn, "r")
			rawtext = str(f.readlines())
			f.close()
			return rawtext
		except FileNotFoundError:
			print ("Error: File does not appear to exist. Defaulting to \"test-ips.txt\"")
			f = open('test-ips.txt', "r")
			rawtext = str(f.readlines())
			f.close()      
			return rawtext
	else:
		print ("### Error: File does not appear to exist. Defaulting to \"test-ips.txt\" ###")
		f = open('test-ips.txt', "r")
		rawtext = str(f.readlines())
		f.close()
		return rawtext

def main():
	ipradar = ipRadar()
	ipradar.print_app_name()

	# Open file
	filename = input('Enter local file name: ')
	print()
	rawtext = FileOpen(filename)

	ip_address = r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'
	ip_match = re.findall(ip_address, rawtext)

	for ip in ip_match:
		print()
		print("-----------------------------------------------")
		print(ip)

		url = 'http://ipinfo.io/' + str(ip)	

		try:	
			response = urllib.request.urlopen(url)
			data = json.load(response)

			ipaddr = data['ip']
			org = data['org']
			city = data['city']
			country = data['country']
			region = data['region']

			print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org, region, country, city, ipaddr))
			print('')
		except:
			print (ip + ', error.')
			print('')
			pass

if __name__ == '__main__':
	main()