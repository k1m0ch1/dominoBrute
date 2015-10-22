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

response = browser.open('http://mail.postel.go.id/')
browser.select_form(nr=0)
browser.form['Username'] = 'user'
browser.form['Password'] = 'password'
response = browser.submit()

while paging==True:
	inject = 'http://mail.postel.go.id/names.nsf/74eeb4310586c7d885256a7d00693f10?ReadForm&TemplateType=2&TargetUNID=85255E01001356A8852554C200753106&Seq={0}&Start={1}' .format(pagefrom,page)
	print inject
	response = browser.open(inject)
	html = BeautifulSoup(response.read())
	nyari = html.body.find_all('a',href=True)

	while b==True:
		if a==112:
			b=False
		else:
			d[c] = 'https://mail.postel.go.id' + nyari[a].get('href')
			a+=3
			c+=1

	for a in range(0,33):
		response = browser.open(d[a])
		html = BeautifulSoup(response.read())
		mail = ""
		email = ""

		for usr in html.body.find_all('table',{'id':'Person_Mail'}):
			aw = usr.find_all('font',{'size':'2'})
		if len(aw[8].contents) >0:
			usr = aw[8].contents
			mail = aw[8].contents[0]
		else:
			usr = aw[12].contents[0].split('@')[0]

		if len(aw[12].contents)>0:
			email = aw[12].contents[0]
			usr = aw[12].contents[0].split('@')[0]

		#usr = html.body.find_all(attrs={"name": "$dspInternetAddress"})[0]['value']
		#password = html.body.find_all(attrs={"name": "$dspHTTPPassword"})[0]['value']
		print "{0} == {1} == {2}".format(mail, usr, email)
		with open("listuser", "a") as text_file:
			text_file.write("{0}\n" .format(usr))
		with open("listuser3", "a") as text_file:
			text_file.write("{0} == {1} == {2}\n".format(mail, usr, email))

	page += pageadding
	pagefrom += 1
	print 'next page'
	b=True
	c=0
	a=13

	if page==pagelast:
		paging=False
