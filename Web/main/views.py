from django.shortcuts import render
from django.http import HttpResponse
import main.functions as db
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from main.models import User
from main.forms import NewUserForm
from django.contrib.auth import logout
from django.contrib.auth import login


class RegisterView(FormView):

    template_name = 'register.html'
    form_class = NewUserForm
   
    def form_valid(self, form): 
        print(form)
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

def Logout_view(request):
    logout(request)
    return redirect('/')


def index(request):
    return render(request,'base.html')

def team(request):
   return render(request,'team.html')



def NotFound(request, exception=None):
    return render(request,'404.html',status=404)

