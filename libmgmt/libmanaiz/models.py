from django.db import models

class Book(models.Model):
	book_title = models.CharField(max_length = 250)
	pub_date = models.DateTimeField()
	author = models.CharField(max_length = 250)
	publisher = models.CharField(max_length = 250)
	isbn = models.IntegerField()
	language = models.CharField(max_length = 50)
	no_of_pages = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__ (self):
		return self.book_title

class Patron(models.Model):
	name = models.CharField(max_length = 300)

	def __str__(self):
		return self.name

class Borrow(models.Model):
	book = models.ForeignKey(Book)
	borrowed_by = models.ForeignKey(Patron)
	borrowed_date = models.DateTimeField()
	borrowed_reason = models.CharField(default='No reason provided', max_length=1000)

	def __str__(self):
		return self.borrowed_by