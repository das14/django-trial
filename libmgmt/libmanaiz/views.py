from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Book, Comment
from .forms import AddBookForm

import urllib

def index(request):
	template = loader.get_template('libmanaiz/index.html')
	popular_book = Comment.objects.order_by('rating_value')
	recently_added = Book.objects.order_by('date_added')[:6:-1]
	context = RequestContext(request, {
		'recently_added': recently_added,
		'popular_book': popular_book,
	})
	return HttpResponse(template.render(context))

def all_books(request):
	template = loader.get_template('libmanaiz/all_books.html')
	all_books = Book.objects.order_by('book_title')
	context = RequestContext(request, {
		'all_books': all_books,
	})
	return HttpResponse(template.render(context))

def test(request):
	template = loader.get_template('libmanaiz/test.html')
	return HttpResponse(template.render())

def add_book_form_upload(request):
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

			print ("image_link = ", image_link)

			if image_link == "":
				# Set image to default image
				image_link = "http://www.clker.com/cliparts/6/4/J/9/E/9/closed-book-md.png"

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