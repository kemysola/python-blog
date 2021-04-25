from django.urls import path, include
from django.conf.urls import url 
from django.conf import settings
from articles import views as article_views
from django. urls import reverse_lazy
#from django .contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', article_views.article_list),
    path('accounts/',include('accounts.urls')),
    path('articles/',include('articles.urls')),
    #path('users/',include('users.urls')),
    
    #path('logins/', views.logins),
    #path('contact/', views.contact),
    #path('comment/', views.comment),
    #path('accounts/', include('django.contrib.auth.urls')),
    


]

