#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : config.py                          #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

import requests

class Config:
	def loadCookie(self):
		try:
			file = open('log/cookies.log','r')
			cookie = file.read()
			file.close()
			return cookie.strip()
		except IOError:
			return False

	def banner(self):
		return '''\n
\033[1;93m█████████
\033[1;93m█▄█████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬●
\033[1;93m█\033[1;91m▼▼▼▼▼ \033[1;92m- _ --_--\033[1;95m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ _𝟑𝟕𝟖
\033[1;93m█ \033[1;95m \033[1;95m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;93m█\033[1;91m▲▲▲▲▲\033[1;93m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝\033[1;91m •\033[1;93m•\033[1;92m• \033[1;91m𝐂𝐘𝐁𝐄𝐑•𝐆𝐇𝐎𝐒𝐓_𝟑𝟕𝟖 \033[1;92m•\033[1;93m•\033[1;91m•
\033[1;96m█████████      \033[1;92m«------------✧------------»
\033[1;92m ██ ██   \033[1;91m•\033[1;93m•\033[1;92m• \033[1;95mDEVELOPMEN BY MASLAKHUDIN LATIF \033[1;92m•\033[1;93m•\033[1;91m•
\033[1;94m_________________________________________________________

\033[1;97m{\033[1;91m+\033[1;97m} AUTHOR     : MASLAKHUDIN LATIF
\033[1;97m{\033[1;91m+\033[1;97m} GITHUB     : https://github.com/DARKFACEBOOK378/L4TIF
\033[1;97m{\033[1;91m+\033[1;97m} FACEBOOK   : https://www.facebook.com/LATIF.DEV.378
\033[1;97m{\033[1;91m+\033[1;97m} WHATSAPP   : 0895323602XXX
\033[1;97m{\033[1;91m+\033[1;97m} MY TEAM    : CyberGhost_378
\033[1;94m_________________________________________________________'''

	def httpRequest(self, url, cookies):
		try:
			return requests.get(url, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')

	def httpRequestPost(self, url, cookies, params):
		try:
			return requests.post(url, data = params, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')
