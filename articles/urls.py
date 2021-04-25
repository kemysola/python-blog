from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

#from django .contrib.auth import views as auth_views

app_name = 'articles'

urlpatterns = [
    path('',views.article_list, name ='list'),
    url(r'^create/$',views.article_create, name = 'create'),
    #url(r'^(?P<slug>[\w-]+)/$',views.article_details,name ='detail'),
    path('<slug:slug>/',views.article_details,name ='detail'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name ='accounts/password_reset_change.html')),
]
 