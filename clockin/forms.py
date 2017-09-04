
from django import forms
from .models import Work
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton
from django.forms import extras

class WorkForm(forms.ModelForm):

    class Meta:

        model = Work
        fields = ('intern', 'date','time_in', 'time_out', 'summary')
      
        widgets = {
          'date' : extras.SelectDateWidget(empty_label="Nothing"),

          
        }

class WorkListFormHelper(FormHelper):    
    form_method = 'GET'
    field_template = 'bootstrap3/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    layout = Layout(
    	 Fieldset(
                    '<i class="fa fa-search"></i> Search Time Logs',       
                	'intern',
                  'date_between'
                ),
    			#'resource_first_name',
             	#'resource_last_name',
             	#'HUBzone',
             	#'employment_status',
              Submit('submit', 'Apply Filter'),
    )
class ClockoutForm(forms.ModelForm):
    summary = forms.CharField( widget=forms.Textarea )
    class Meta:

        model = Work
        fields = ('summary',)
        
class ClockinForm(forms.ModelForm):
    class Meta:

        model = Work
        fields = ()



