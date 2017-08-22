#coding=utf-8
#!/usr/bin/env python

# Program design to warn the user to take regular breaks during the day
# Duration of break and focused times can be changed

import webbrowser
import time

total = 10
breaks = 0
interval_min = 25 # Minutes before break
free_min = 15 # Minutes during break

free_seconds = free_min*60
interval_seconds = interval_min*60

while(breaks < total):
	time.sleep(interval_seconds)
	webbrowser.open("https://www.youtube.com/watch?v=qYnA9wWFHLI")
	time.sleep(free_seconds)
	webbrowser.open("https://www.youtube.com/watch?v=iNpXCzaWW1s")
	breaks += 1
