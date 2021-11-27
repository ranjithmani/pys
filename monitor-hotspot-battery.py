#!/usr/bin/python3.8
#
# This script will notify you once your jio hotspot battery charge level goes below 10%
# schedule this scripts on your cron 
#
import requests
from bs4 import BeautifulSoup
import notify2

url = 'http://jiofi.local.html/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
x = soup.find_all('input')[3]["value"]
y = x.replace("%", "")

def mynotify():
    notify2.init("Battery Notifier")
    n = notify2.Notification(None, message='Battery usage', icon='/home/rmani/Downloads/red.png')
    n.set_timeout(10000)
    n.update('Hotspot Battery Critical', 'Current charge level is '+ y+'%')
    n.show()

if y < '10':
    mynotify()
