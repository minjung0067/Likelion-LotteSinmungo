
from django.shortcuts import render, redirect , get_object_or_404
from .forms import ProblemForm, SigninForm, SignupForm
from .models import Problem , myUser
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.hashers import make_password, check_password 
from django.http import HttpResponse

from django.views.generic.list import ListView



def index(request):
    user_id = request.session.get('user')
    if user_id :
        myuser_info = myUser.objects.get(pk=user_id)  #pk : primary key
        return render(request, 'index.html', {'user':myuser_info}) 
    return render(request, 'index.html')

def problemDetail(request, problem_detial_id):
    problem_detail_obj = get_object_or_404(Problem, pk = problem_detial_id)
    return render(request, 'problem_detail.html', {"problem_detail_key":problem_detail_obj})

def problemList(request):
    problem_list_item = Problem.objects.all()
    return render(request, 'problemList.html', {'problem_list_item':problem_list_item})

def solution(request):
    return render(request, 'solution.html')

def writing(request):
    if request.method == "POST":
        filled_form = ProblemForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('problemList') #problemList 중에서도 최신 순으로 나열되어 있는 페이지를 보여주는 게 좋을듯 (나중에 추가하자)
    prb_form = ProblemForm()
    return render(request, 'writing.html', {'prb_form':prb_form})

def signup(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        username = request.POST.get('username',None)   #딕셔너리형태
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        res_data = {} 
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            user = myUser(username=username, password=make_password(password))
            user.save()
            return render(request,'index.html')
        return render(request, 'signup.html', res_data) #register를 요청받으면 register.html 로 응답.

def signin(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'signin.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)


        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            myuser = get_object_or_404(myUser,username=login_username)
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(login_password, myuser.password):
                request.session['user'] = myuser.id 
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'signin.html',response_data)

def signout(request): #logout 기능
    logout(request) #logout을 수행한다.
    return HttpResponseRedirect(reverse('index'))

def mypage(request):
    return render(request, 'mypage.html')