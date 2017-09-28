import django_filters
from .models import *
from django import forms
from dal import autocomplete


class WorkListFilter(django_filters.FilterSet):
	date_between = django_filters.DateFromToRangeFilter(name='date',label='Pay Period (MM/DD/YY)', widget=django_filters.widgets.RangeWidget())

	intern= django_filters.ModelChoiceFilter(name='intern', label='Intern',queryset=Intern.objects.all(), widget=autocomplete.ModelSelect2(url='intern-autocomplete'))

	class Meta:
		model = Work
		fields =  ('intern',)
		order_by = ['intern__FName']