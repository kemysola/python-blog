from django.urls import path , include
from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django. urls import reverse_lazy


app_name = 'accounts'


urlpatterns = [
    url(r'^signup/$', views.signup_view, name= 'signup'),
    url(r'^login/$', views.login_view, name= 'login'),
    url(r'^logout/$', views.logout_view, name= 'logout'),
    #path('accounts/', include('django.contrib.auth.urls')),
    
    
]
