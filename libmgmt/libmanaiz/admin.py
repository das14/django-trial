from django.contrib import admin
from .models import Book, Borrow, Patron, Comment

#class BookAdmin(admin.ModelAdmin):
#	fields = ['isbn', 'book_title', 'pub_date']

#admin.site.register(Book, BookAdmin)

admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Patron)
admin.site.register(Comment)
