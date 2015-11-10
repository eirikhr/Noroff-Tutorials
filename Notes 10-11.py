"""

import math
print(math.pow(4,2))
print(math.sqrt(9))
print("Pi = ", math.pi)
print("e = ", math.e)

# OR
print("\nOr by importing the constant in modules available directly like this:\n")

from math import pow, sqrt, pi, e

print(pow(4,2))
print(sqrt(9))
print(pi)
print(e)

# Productivity Alarm
import time
import webbrowser

music_video = "https://www.youtube.com/watch?v=YQHsXMglC9A&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI&index=1"
total_breaks = 3
break_count = 0
sleep_time = 3

while break_count < total_breaks:
    time.sleep(sleep_time)
    webbrowser.open(music_video)
    break_count += 1                            #Instead of break_count = break_count + 1
"""

#HelloMachine
while True:
    name = input("Enter your name: ")
    if name == "stop" : break
    town = input("Where are you from? ")
    print("Hello ", name, "from ", town)
