from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.translation import gettext as _
from django.forms import ModelForm
from django.utils import timezone
#from django_filters import rest_framework as filters







class Intern(models.Model):
	def __str__(self):
   		return self.FName + " " + self.LName

	FName = models.CharField(_("First Name"), max_length = 50, default = None)
	LName = models.CharField(_("Last Name"), max_length = 50, default = None)
	username = models.CharField(_("Username"), max_length = 50, default = None)
#added for autocomplete
	def __iter__(self):
		for field in self._meta.get_fields(include_parents=True, include_hidden=False):
			value = getattr(self, field.name, None)

			yield (field, value)

class Work(models.Model):
	user = models.CharField(_("User"),  max_length = 50, default = None)
	intern = models.ForeignKey("Intern", default = 1)
	date = models.DateField(_("Date"), default= datetime.date.today, blank=True)
	time_in = models.TimeField(_("Time In"),default= datetime.datetime.now().time(), blank=True)
	time_out = models.TimeField(_("Time Out"),default= datetime.datetime.now().time(), blank=True)
	active_session = models.BooleanField(_("Active Session"),default = True)
	summary = models.CharField(_("Summary"), max_length = 5000, default = "N/A")
	duration = models.DecimalField(_("Duration"), max_digits = 10, decimal_places = 2, default = 0)




















