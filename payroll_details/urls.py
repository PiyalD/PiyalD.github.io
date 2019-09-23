from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^empid(?P<emp_id>[0-9]+)/mail', views.sal_mail, name="emp_salary_mail"),
    url(r'^empid(?P<emp_id>[0-9]+)/salarydetails', views.sal, name="emp_salary_det"),
    url(r'^empid(?P<emp_id>[0-9]+)/salary', views.salary_details, name="emp_salary"),
    url(r'^empid(?P<emp_id>[0-9]+)/$', views.emp_details, name='empdetails')
]
