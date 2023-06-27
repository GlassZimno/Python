#Dominik Zimny
#29/11/2019

import webbrowser
import time
import random

while True:
    sites = random.choice([
        'google.com',
        'mastercode.online',
        'youtube.com'
        ])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)
