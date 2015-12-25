from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
    url(r'^about', views.test),
    url(r'^add_book', views.add_book_form_upload),
	url(r'^all_books', views.all_books),
]
