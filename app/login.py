#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : login.py                           #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

import os, time
from src import language

def loginFb(self, url, config):
	os.system('clear')
	print(config.banner())
	print('\n\033[1;95m[©] Login Pakai Cookie FB Kalian : [©]\n')
	while True:
		cookies = raw_input('TEMPEL COOKIE DI SINI -->: ')
		response = config.httpRequest(url, cookies).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			print('\n\033[0;92m SABAR DULU NGENTOT LAGI PROSES...')
			language.main(cookies, url, config)
			try: os.mkdir('log')
			except: pass
			save = open('log/cookies.log','w')
			save.write(cookies.strip())
			save.close()
			print('\n\033[0;92mTuh Kan Login Berhasil✓\033[0m')
			time.sleep(2)
			break
		else:
			print('\n\033[0;91mCOOKIE MODAR!, COBA LAGI! .\n\033[0m')
