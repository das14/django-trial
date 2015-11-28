from django.db import models
from django.core.validators import MaxValueValidator

class Book(models.Model):
	book_title = models.CharField(max_length = 250)
	pub_date = models.DateTimeField()
	author = models.CharField(max_length = 250)
	publisher = models.CharField(max_length = 250)
	isbn = models.PositiveIntegerField()
	language = models.CharField(max_length = 50)
	no_of_pages = models.PositiveIntegerField()
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__ (self):
		return self.book_title

class Patron(models.Model):
	name = models.CharField(max_length = 300)

	def __str__(self):
		return self.name

class Borrow(models.Model):
	book_borrowed = models.ForeignKey(Book)
	borrowed_by = models.ForeignKey(Patron)
	borrowed_date = models.DateTimeField()
	borrowed_reason = models.CharField(default='No reason provided', max_length=1000)

	def __str__(self):
		return self.borrowed_reason

class Comment(models.Model):
   	rating_book = models.ForeignKey(Book, null = False)
        rating_value = models.PositiveIntegerField(validators = [MaxValueValidator(10)])
        date_of_rating = models.DateTimeField(auto_now_add = True)
        rating_by = models.ForeignKey(Patron)
        
        def __str__(self):
                return self.rating_value
