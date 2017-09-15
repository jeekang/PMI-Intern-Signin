from django.conf.urls import url
from .models import Work
from . import views

urlpatterns = [
    url(r'^$', views.work_list, name='index'),
    #url(r'^(?P<work_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^home/$', views.work_list, name= 'home'),
    url(r'^start_shift/$', views.add_new, name= 'add'),
    url(r'^edit/(?P<work_id>\d+)/$', views.clockout, name='end_work_session'),
    url(r'^delete/(?P<pk>\d+)/$', views.workDelete.as_view(model = Work), name="work_delete"),
    #url(r'^test/$', views.WorkListView.as_view(), name="person_list_2"),
    url(r'^adminhome/$', views.AdminView, name= 'adminhome'),
    url(r'^logout/$', views.logout_page, name = 'logout'),
    url(r'^history/$', views.past_time, name= 'past'),
    url(r'^admin_edit/(?P<work_id>\d+)/$', views.edit_hours, name='edit_hours'),
    url(r'^new_hours/$', views.add_work, name= 'add_work'),






]
