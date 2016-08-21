#!/usr/bin/env python
#-*-coding:utf-8 -*-

import wikitools
import sys

wiki_url="https://bn.wikipedia.org/w/api.php"

wiki_username="JoyBot"
wiki_password="sonamoni@1861"

wiki=wikitools.wiki.Wiki(wiki_url)

login_result=wiki.login(username=wiki_username,password=wiki_password)

if login_result==True:
    print "Logged in."

else:
    print"Invalid user name and password"
    sys.exit()

pagename="User:"+wiki_username+"/test"

content="this the test page of manny conttent"

page=wikitools.Page(wiki,pagename,followRedir=True)

old_content= page.getWikiText()

new_content=old_content.replace("manny","many").replace("conttent","content")

    
print page

page.edit(text=new_content,summery="test edit")

users=["JoyBot"]

conten=""

for name in users:
	user=wikitools.User(wiki,name)
	content=content+name+"has edited"+str(user.editcount)+"pages"+"\n"


page=wikitools.Page(wiki,pagename,followRedir=True)
page.edit(text=content,summery="test edit")



