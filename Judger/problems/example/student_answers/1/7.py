#!/usr/bin/python3

import sys
import os
import time

def spab(x):
 for abc in range(x):
  print(' ')
print('''pengubah versi bahasa programming

1.python

2.java

by kevin A ''')

spab(5)
pilih = input('angka: ')
pilih = int(pilih)
spab(5)
skr = os.getcwd()
print('anda sekarang ada di ' + skr)
spab(5)
dirs = '/media/kevin/data/programming/python_saya/'
if (str(skr)) != (str(dirs)):
 print('sedang tidak di python_saya')
 time.sleep(0.5)
 print('merubah ke python_saya')
 os.chdir(dirs)
 eko = os.getcwd()
 print('dan sekarang ada di ' + eko)


if pilih == 1:
 py = os.access('changepyversion.sh', os.W_OK)
 if py == False:
  print('file changepyversion.sh ga ada')
  sys.exit()
 os.system('chmod 777 changepyversion.sh')
 os.system('./changepyversion.sh')
 spab(5)
 os.system('python --version')

if pilih == 2:
# jav = os.access('changejavaversion.sh', os.W_OK)
# if jav == False:
#  print('file changejavaversion.sh ga ada')
#  sys.exit()
# java = os.access('changejavacversion.sh', os.W_OK)
# if java == False:
#  print('WARNING: file changejavacversion.sh ga ada')
#  time.sleep(2)

 os.system('sudo update-alternatives --config java') 
 os.system('sudo update-alternatives --config javac')
 spab(5)
 os.system('java -version')



