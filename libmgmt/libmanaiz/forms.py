from django import forms

class AddBookForm(forms.Form):
	book_title = forms.CharField(max_length = 250)
	publication_month = forms.IntegerField()
	publication_day = forms.IntegerField()
	publication_year = forms.IntegerField()
	author = forms.CharField(max_length = 250)
	publisher = forms.CharField(max_length = 250)
	isbn = forms.IntegerField(required = False)
	language = forms.CharField(max_length = 50)
	number_of_pages = forms.IntegerField()
	number_of_copies = forms.IntegerField()
	image_link = forms.CharField(max_length = 1000, required = False)

class LogInForm(forms.Form):
	username = forms.CharField(max_length = 100)
	password = forms.CharField(max_length = 100)

class SignUpForm(forms.Form):
	firstName = forms.CharField(max_length = 100)
	lastName = forms.CharField(max_length = 100)
	email = forms.EmailField(max_length = 100)
	userName = forms.CharField(max_length = 100)
	passWord = forms.CharField(max_length = 100)