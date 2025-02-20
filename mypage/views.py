import bcrypt
from django.shortcuts import render, redirect
from user.models import User

# Create your views here.
def mypageIndex(request):
    return render(request, 'mypage/mypage.html')


def mypageAdmin(request):
    return render(request, 'mypage/myadminmain.html')


def consulting(request):
    return render(request, 'mypage/consulting.html')


def passwordUpdate(request):
    session_user = request.session['user']
    print("session_user", session_user)

    if request.method == 'POST':
        if User.objects.filter(email=session_user).exists():
            user = User.objects.get(email=session_user)
            user_password = user.password.encode('utf=8')

            if bcrypt.checkpw(request.POST['nowpwd'].encode('utf=8'), user_password):
                update_password = request.POST['updatepwd']
                hashed_password = bcrypt.hashpw(update_password.encode('utf=8'), bcrypt.gensalt())
                user.password=hashed_password.decode('utf=8')
                user.save()
                return redirect('mypage')

            return render(request, "mypage/password.html")
    else:
        return render(request, 'mypage/password.html')


def userinfoUpdate(request):
    return render(request, 'mypage/userinfo.html')
