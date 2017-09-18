#NOT USED


import django_tables2 as tables
from django_tables2.utils import A
from .models import Work

class WorkTable(tables.Table):
	End_Session = tables.LinkColumn('item_edit', text='End Session', args=[A('pk')], orderable=False,empty_values=())

	def render_name(self, value, record):
		url = record.get_absolute_url()
		return mark_safe('<a href="%s">%s</a>' % (url, record))

	class Meta:
		model = Work

		attrs = {"class": "table-striped table-bordered", 'width':'100%'}
		empty_text = "You do not currently have any active sessions."
