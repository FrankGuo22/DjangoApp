from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
import MySQLdb
# Create your views here.
def search_form(request):
	return render(request,'search-form.html')
	
def search(request):
	if 'q' in request.GET and request.method=='GET':
		q = request.GET['q']
		db = MySQLdb.connect( user = 'root', db = 'zong', passwd = 'FrankGuo', host ='127.0.0.1')
		cursor1 = db.cursor()
		n= cursor1.execute("select userPassword from admininfo where userID="+"'"+ q +"';")
		name = cursor1.fetchall()
		return render(request, 'search-now.html',{'name': name, 'query': q})
	else:
		return HttpResponse('Please submit a search term.')