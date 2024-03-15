from django.shortcuts import render
from django.http import HttpResponse
import main.functions as db
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from main.models import User


class RegisterView(CreateView):
    model = User

    template_name = 'register.html'
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def check_login(cookie):
    if cookie and 'login' in cookie:
        return db.get_user(cookie['login'])
    return None

def index(request):
    user = check_login(request.COOKIES)
    if user:
        return render(request,'base.html', {'user_login':user['nickname']})
    else:
         return render(request,'base.html')

def team(request):
    user = check_login(request.COOKIES)
    if user:

        return render(request,'team.html', {'user_login':user['nickname']})
    else:
        return render(request,'team.html')

def create_cookie(request):
    data = {'login':'test','nickname':'adolf','password':'mega_gay'}
    try:
        db.delete_user(data['login'])
    except:
        pass
    db.add_user(data)

    response = redirect('/')
    response.set_cookie('login',data['login'])
    return response


def NotFound(request, exception=None):
    user = check_login(request.COOKIES)
    if user:
        return render(request,'404.html',{'user_login':user['nickname']},status=404)
    else:
        return render(request,'404.html',status=404)
    
def Settings(request):
    user = check_login(request.COOKIES)
    if user:

        return render(request,'settings.html', {'user_login':user['nickname']})
    else:
        return render(request,'settings.html')

