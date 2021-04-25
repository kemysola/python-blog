from django.shortcuts import render
from django.http import HttpResponse
from django. urls import reverse_lazy



# Create your views here.
def home(request):
    return render(request,'accounts/dashboard.html')





'''
-- myblogs
---- templates
------ accounts
----------dashboard.html
-------------   comments.html
-------------- login.html
----------------- register.html
'''


    