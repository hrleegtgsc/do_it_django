import bcrypt
import jwt
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from do_it_django_prj.settings import SECRET_KEY
from .models import UserInfo


# Create your views here.

def index(request):
    return render(request, 'userInfo/index.html')
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())


def login(request):
    if request.method == 'POST':
        if UserInfo.objects.filter(email=request.POST['email']).exists():
            user = UserInfo.objects.get(email=request.POST['email'])
            user_password = user.password.encode('utf=8')

            if bcrypt.checkpw(request.POST['password'].encode('utf=8'), user_password):
                token =jwt.encode({"id":user.email}, SECRET_KEY, algorithm="HS256")
                request.session['user']=user.email
                return redirect("index")

            return render(request, "userInfo/login.html")
    else:
        return render(request, "userInfo/login.html")



def join(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordCheck']:
            password_not_hashed = request.POST['password']
            hashed_password = bcrypt.hashpw(password_not_hashed.encode('utf=8'), bcrypt.gensalt())
            UserInfo(
                email=request.POST['email'],
                password=hashed_password.decode('utf=8'),
                name=request.POST['name'],
                nickname=request.POST['nickname'],
                role=request.POST['gender']
            ).save()
            return redirect('/userInfo/login.html')
        return render(request, 'userInfo/join.html')
    else:
        form = UserCreationForm
        return render(request, 'userInfo/join.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('login')
