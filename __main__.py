#!/usr/bin/env python3

from zipfile import ZipFile
from time import sleep
from sys import argv


def zip_cracker(src=None, pass_list=None):   
  if (src != None):
    if (pass_list != None):
      try:
        zip, passwd = ZipFile(str(r'%s'%src)) , open(r'%s'%pass_list,'r+').readlines()
      
      except:
        quit("Error -> opening_file")

      for passwords in passwd:
        password = passwords.strip('\n')
        sleep(.02)
        
        try:
          zip.extractall(pwd=bytes(password, 'utf-8'))
          print('\r\n  [*] Password Found -> %s\n'%password)
          break

        except:
          print('\r\n  [!] PassWord Not Found -> %s\n'%password)
      
    else:
      try:
        ZipFile(str(r'%s'%src)).extractall()
        print('\r\n  [*] Password Found -> (None)\n')

      except:
        quit("Error -> extracting")

  else:
    quit("Error -> params")


try:
  zip_file, password_list = argv[1:3]

except ValueError:
  try:
    zip_file, password_list = argv[1], ''

  except ValueError:
    quit("Error -> argv")

zip_cracker(zip_file, password_list)
