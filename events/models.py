from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Venue(models.Model):
	name = models.CharField('Venue Name', max_length=120)
	address = models.CharField(max_length=300)
	zip_code = models.CharField('Zip Code', max_length=15)
	phone = models.CharField('Contact Phone', max_length=25, blank=True)
	web = models.URLField('Website Address', blank=True)
	email_address = models.EmailField('Email Address', blank=True)
	owner = models.IntegerField("Venue Owner", blank=False, default=1)
	venue_image = models.ImageField(null=True, blank=True, upload_to="images/")
	
	def __str__(self):
		return self.name


class MyClubUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField('User Email')

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	event_date = models.DateTimeField('Event Date')
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(MyClubUser, blank=True)
	approved = models.BooleanField('Aprroved', default=False)

	def __str__(self):
		return self.name

	@property
	def Days_till(self):
		today = date.today()
		days_till = self.event_date.date() - today
		days_till_stripped = str(days_till).split(",", 1)[0]
		return days_till_stripped
	
	@property
	def Is_Past(self):
		today = date.today()
		if self.event_date.date() < today:
			thing = "Past"
		else:
			thing = "Future"
		return thing