from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Book

def index(request):
        template = loader.get_template('libmanaiz/index.html')
        #popular_book = Book.
        recently_added = Book.objects.order_by('date_added')[:6]
        context = RequestContext(request, {
                'recently_added': recently_added,
        })
	return HttpResponse(template.render(context))

def test(request):
        template = loader.get_template('libmanaiz/test.html')
        return HttpResponse(template.render())
