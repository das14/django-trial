from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Template
from django.contrib.auth import authenticate, login, logout

from .models import Book, Comment
from .forms import *

import urllib
from PIL import Image

def index(request):
	template = loader.get_template('libmanaiz/index.html')
	popular_book = Comment.objects.order_by('rating_value')
	recently_added = Book.objects.order_by('date_added')[::-1]
	recently_added = recently_added[:6]

	logged_in = request.user.is_authenticated()

	context = RequestContext(request, {
		'recently_added': recently_added,
		'popular_book': popular_book,
		'logged_in': logged_in,
	})
	return HttpResponse(template.render(context))

def all_books(request):
	template = loader.get_template('libmanaiz/all_books.html')
	all_books = Book.objects.order_by('book_title')

	logged_in = request.user.is_authenticated()

	context = RequestContext(request, {
		'all_books': all_books,
		'logged_in': logged_in,
	})
	return HttpResponse(template.render(context))

def test(request):
	template = loader.get_template('libmanaiz/test.html')
	return HttpResponse(template.render())

def book_page(request, book_title):
	book_title = book_title.replace('-', ' ').replace('_', ' ')
	book = Book.objects.filter(book_title = book_title)
	template = loader.get_template('libmanaiz/individual_book.html')

	logged_in = request.user.is_authenticated()

	context = RequestContext(request, {
		'book': book,
		'logged_in': logged_in,
	})
	return HttpResponse(template.render(context))

def add_book_form_upload(request):
	if request.user.is_authenticated():
		if request.method == 'GET':
			form = AddBookForm()
		else:
			form = AddBookForm(request.POST) # Bind data from request.POST into a PostForm

			if form.is_valid():
				book_title = form.cleaned_data['book_title']
				publication_day = form.cleaned_data['publication_day']
				publication_month = form.cleaned_data['publication_month']
				publication_year = form.cleaned_data['publication_year']
				author = form.cleaned_data['author']
				publisher = form.cleaned_data['publisher']
				isbn = form.cleaned_data['isbn']
				language = form.cleaned_data['language']
				number_of_pages = form.cleaned_data['number_of_pages']
				number_of_copies = form.cleaned_data['number_of_copies']
				image_link = form.cleaned_data['image_link']

				if image_link == "":
					# Set image to default image
					image_link = "http://www.clker.com/cliparts/6/4/J/9/E/9/closed-book-md.png"

				try:
					size = 500, 400
					urllib.urlretrieve(image_link, "/home/jeet/projects/Django Library Project/django-trial/libmgmt/libmanaiz/images/" + book_title)

					try:
						im = Image.open("/home/jeet/projects/Django Library Project/django-trial/libmgmt/libmanaiz/images/" + book_title)
						im.thumbnail(size, Image.ANTIALIAS)
						im.save("/home/jeet/projects/Django Library Project/django-trial/libmgmt/libmanaiz/images/" + book_title, "JPEG")
					except IOError:
						print "############################# cannot create thumbnail"
				except Exception, e:
					print (e)

				new_book = Book.objects.create(
					book_title = book_title,
					pub_date = str(publication_year) + "-" + str(publication_month) + "-" + str(publication_day),
					author = author,
					publisher = publisher,
					isbn = isbn,
					language = language,
					no_of_pages = number_of_pages,
					number_of_copies = number_of_copies,
					image_link = image_link)

				return HttpResponseRedirect('/')
		return render(request, 'libmanaiz/add_book.html', {
			'form': form,
			})
	return HttpResponseRedirect('/')

def image(request, image_title):
	image_data = open("/home/jeet/projects/Django Library Project/django-trial/libmgmt/libmanaiz/images/" + image_title, "rb").read()
	return HttpResponse(image_data, content_type="image/png")

def log_user_in(request):
	if not request.user.is_authenticated():
		if request.method == 'GET':
			form = LogInForm()
		else:
			form = LogInForm(request.POST) 

			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']

				user = authenticate(username = username, password = password)
				if user is not None:
					if user.is_active:
						login(request, user)
					else:
						return HttpResponseRedirect('/not_active')
				return HttpResponseRedirect('/')
		return render(request, 'libmanaiz/login.html', {
			'form': form,
			})
	return HttpResponseRedirect('/')

def log_user_out(request):
	if request.user.is_authenticated():
		logout(request)
	return HttpResponseRedirect('/')