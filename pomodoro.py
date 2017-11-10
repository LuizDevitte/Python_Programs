#coding=utf-8
#!/usr/bin/env python

from webbrowser import open as Open
from time import sleep
from sys import argv

total_breaks = argv[1]
breaks = 0
interval_min = 25 	# Minutes before break
free_min = 5 		# Minutes during break

free_seconds = free_min*60
interval_seconds = interval_min*60

while(breaks < total_breaks):
	sleep(interval_seconds)
	Open("https://www.youtube.com/watch?v=qYnA9wWFHLI")
	sleep(free_seconds)
	Open("https://www.youtube.com/watch?v=iNpXCzaWW1s")
	breaks += 1
