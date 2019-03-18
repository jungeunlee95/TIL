from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# '/users/'   =>  홈페이지
# '/users/login/' => login
def home(request):
    return render(request, 'users/home.html')

def login_user(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    elif request.method == 'POST':
        # 만약 username, paseeword로 넘어온 값이 DB에 저장된 값과 같다면, 로그인!!!
        # 로그인 유저 검증
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # 로그인 성공
            login(request, user)
            messages.success(request, "성공적으로 로그인 되었습니다.")
            return redirect('users:home')
        else:
            # 로그인 실패
            messages.success(request, "로그인에 실패했습니다. 다시 시도해주세요.")
            return redirect('users:login')

def logout_user(request):
    logout(request)
    messages.success(request, "로그아웃 되었습니다.")
    return redirect('users:home')



