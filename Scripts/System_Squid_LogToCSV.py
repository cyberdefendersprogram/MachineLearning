# -*- coding: utf-8 -*-
"""
Created on Mon Aug 09 11:50:42 2018

@author: tienz
"""

# Create a log file into a csv file so we can manipulate it with pandas

import csv
import os 

path = "access.log"
result = [["time", "elapsed", "remotehost", "code/status", "bytes", "method", "URL", "rfc931", "peerstatus/peerhost", "type"]]


with open('access.csv', 'w+', newline='') as csvfile:
	w = csv.writer(csvfile, dialect='excel')
	with open(path, encoding='utf-8') as file:
		lines = file.read().split('\n')

		for line in lines:
			ele = line.split(' ')
			item=[]
			for it in ele:
				if not it == "":
					if it == "-":
						item.append("")
					else:
						item.append(it)
			result.append(item)
		w.writerows(result)
		

	
