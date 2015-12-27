from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
    url(r'^about', views.test),
    url(r'^login', views.log_user_in),
    url(r'^logout', views.log_user_out),
    url(r'^signup', views.sign_user_up),
    url(r'^add_book', views.add_book_form_upload),
	url(r'^all_books', views.all_books),
	url(r'^book/(?P<book_title>[\w\s-]+)/$', views.book_page),
	url(r'^image/(?P<image_title>[\w\s-]+)/$', views.image),
]