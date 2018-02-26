import os, sys

"""This utility will display detailed information
   and plaintext password for the Windows OS primary
   Wifi network.

   The syntax used: 'python WifiPasswordReader.py "SSID"'

   """

name = sys.argv[1]
os.system('netsh wlan show profile name = "'+name+'" key=clear')
