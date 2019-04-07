from django.conf.urls import url
from testapp import views
from django.views.generic import RedirectView

app_name='testapp'
urlpatterns=[

              url(r'^$',views.user_login,name='user_login'),
              url(r'^user_register/',views.user_register,name='user_register'),
              url(r'^user_result/',views.user_result,name='user_result')

              ]

