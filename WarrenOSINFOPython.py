#!/usr/bin/python3

#~ Name: Warren Justin Chan
#~ Code: S5
#~ Class: CFC3110
#~ Trainer: James

# ~ This OS INFO Script does the following:

# 1. Display OS Version, if Windows then display windows details; if Linux then linux details
# 2. Display private IP address, public IP address, and default gateway
# 3. Display Hard disk size; free and used space
# 4. Display top 5 directories and their size
# 5. Display CPU Usage and refresh every 10 seconds.




import platform

# 1. Display OS Version, if Windows then display windows details; if Linux then linux

print ('This machines OS System is:')
print (platform.platform())

print()
# 2. Display private IP address, public IP address, and default gateway

# Private IP
# Sockets allow communication between two different processes on the same or different machines. 

import socket

# AF_INET -  provides interprocess communication between processes that run on the same system or on different systems.
# SOCK_DGRAM - Provides datagrams, which are connectionless messages of a fixed maximum length. This type of socket is generally used for short messages, such as a name server or time server.

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 	
s.connect(("8.8.8.8", 80))
print('Your Private IP Address is : ', s.getsockname()[0])
s.close()

# Public IP

# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world

import urllib.request

publicip = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')

print('Your Public IP Address is: ', publicip)

# Default Gateway

# Netifaces - Portable network interface information

import netifaces

gateways = netifaces.gateways()
default_gateway = gateways['default'][netifaces.AF_INET][0]
print('Your Default Gateway is : ', default_gateway)

print()
# 3. Display Hard disk size; free and used space

import shutil
print('Disk Space Usage: ')
total, used, free = shutil.disk_usage('/')

#  This // operator divides the first number by the second number and rounds the result down to the nearest integer (or whole number).

print('Size: ',(total // (1024**3)), 'GB') 	
print('Used: ',(used // (1024**3)), 'GB')
print('Free: ',(free // (1024**3)), 'GB')

print()
# 4. Display top 5 directories and their size

import os 

dir_list = next(os.walk('/home/kali'))[1] 		# os.walk is a generator and calling next will get the first result in the form of a 3-tuple (dirpath, dirnames, filenames). Thus the [1] index returns only the dirnames from that tuple
print('Directories in /home/kali are: ', dir_list)

def get_dir_size(path='/home/kali/CFC3110'):
    total = 0
    for p in os.listdir(path):					# os.listdir() returns a list of file and directory names. 
        full_path = os.path.join(path, p) 		# Each file or directory name is joined with the path of the parent directory with os.path.join() to make a full path.
        if os.path.isfile(full_path):
            total += os.path.getsize(full_path) # In the case of a file, the size is retrieved with the st_size attribute of the stat_result object
        elif os.path.isdir(full_path):
            total += get_dir_size(full_path)	# In the case of a directory, this function is called recursively to add all the sizes and return the total size.
    return total

print('Directory size for CFC3110 is: ', get_dir_size(path='/home/kali/CFC3110') , 'bytes')



def get_dir_size(path='/home/kali/Python'):
    total = 0
    for p in os.listdir(path):
        full_path = os.path.join(path, p)
        if os.path.isfile(full_path):
            total += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total += get_dir_size(full_path)
    return total

print('Directory size for Python is: ', get_dir_size(path='/home/kali/Python') , 'bytes')

def get_dir_size(path='/home/kali/nipe'):
    total = 0
    for p in os.listdir(path):
        full_path = os.path.join(path, p)
        if os.path.isfile(full_path):
            total += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total += get_dir_size(full_path)
    return total

print('Directory size for nipe is: ', get_dir_size(path='/home/kali/nipe') , 'bytes')


def get_dir_size(path='/home/kali/SOC'):
    total = 0
    for p in os.listdir(path):
        full_path = os.path.join(path, p)
        if os.path.isfile(full_path):
            total += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total += get_dir_size(full_path)
    return total

print('Directory size for SOC is: ', get_dir_size(path='/home/kali/SOC') , 'bytes')

def get_dir_size(path='/home/kali/trojan'):
    total = 0
    for p in os.listdir(path):
        full_path = os.path.join(path, p)
        if os.path.isfile(full_path):
            total += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total += get_dir_size(full_path)
    return total

print('Directory size for trojan is: ', get_dir_size(path='/home/kali/trojan') , 'bytes')



print()
# 5. Display CPU Usage and refresh every 10 seconds.
print('Displaying CPU Usage (10 second refresh)')
print('Installing psutil')

os.system('pip install psutil')

	
import time
import psutil 	#Python package that retrieves information on ongoing processes and system usage (CPU, memory, storage, network, and sensors)


# While the command is active, sleep for 10 seconds and then run the command again.
while True:
   print("The CPU utilization of all the CPUs is: %s" % (psutil.cpu_percent(interval=2, percpu=True), ))
   time.sleep(10)


# References

#Platform

# https://note.nkmk.me/en/python-platform-system-release-version/

# Socket
# https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
# https://www.ibm.com/docs/en/i/7.3?topic=family-af-inet-address
# https://www.ibm.com/docs/en/aix/7.1?topic=protocols-socket-types

# PublicIP
# https://stackoverflow.com/questions/2311510/getting-a-machines-external-ip-address-with-python

# Decode UTF8
# https://www.digitalocean.com/community/tutorials/python-string-encode-decode

# Default Gateway
# https://stackoverflow.com/questions/53902519/find-default-gateway-address-for-windows-and-linux-on-python

# Netifaces
# https://pypi.org/project/netifaces/

# Hard Disk Size
# https://stackoverflow.com/questions/48929553/get-hard-disk-size-in-python#:~:text=For%20Python%203.3%20and%20above%2C%20you%20can%20use%20the%20shutil,space%20in%20your%20hard%20drive.

# Floor Operator (//)
# https://www.freecodecamp.org/news/what-does-double-slash-mean-in-python/#:~:text=%2C%202022%20%2F%20%23Python-,What%20Does%20%2F%2F%20Mean%20in,Operators%20in%20Python&text=In%20Python%2C%20you%20use%20the,integer%20(or%20whole%20number).

# CPU Usage through psutil
# https://www.educative.io/answers/what-is-psutilcpupercent-in-python
# https://stackoverflow.com/questions/71028846/how-to-get-cpu-stats-every-15-seconds-python

# While and timer command
# https://stackoverflow.com/questions/474528/how-to-repeatedly-execute-a-function-every-x-seconds

# os.walk()
# https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python

# os.join.path() & Code for getting directory size
# https://note.nkmk.me/en/python-os-path-getsize/
