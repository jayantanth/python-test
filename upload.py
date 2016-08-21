#!/usr/bin/env python
#-*-coding:utf-8 -*-

import csv
import wikitools
import sys

wiki_url="https://bn.wikipedia.org/w/api.php"

wiki_username=""
wiki_password=""

wiki=wikitools.wiki.Wiki(wiki_url)

login_result=wiki.login(username=wiki_username,password=wiki_password)

if login_result==True:
    print "Logged in."

else:
    print"Invalid user name and password"
    sys.exit()

pagename="User:"+wiki_username+"/test"


with open('data.csv','rb')as f:
	reader=csv.reader(f)

	for row in reader:
		print row[0]
		print row[1]


		pagename="User:"+wiki_username+"/"+row[0]	
		page=wikitools.Page(wiki,pagename,followRedir=True)
		page.edit(text=row[1],summery="test edit")


