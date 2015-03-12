#coding = uft-8
from django.template.loader import get_template
from django.http import Http404, HttpResponse
import datetime
import time
from django.template import Template, Context
from django.shortcuts import render
import MySQLdb
import os.path

def homepage(req):
	return HttpResponse(time.strftime("%Y-%m-%d %H:%M:%S") + "  Now it's time to open that")
	
def hello(request):
	db = MySQLdb.connect( user = 'root', db = 'zong', passwd = 'FrankGuo', host = '127.0.0.1' )
	cursor1 = db.cursor()
	n= cursor1.execute("select userID from admininfo")
	name = cursor1.fetchall()
	db.close()
	print name
	return render(request,'Now.html',{'name':name})
	
	