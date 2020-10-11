
from django.shortcuts import render, redirect , get_object_or_404
from .forms import ProblemForm
from .models import Problem , myUser ,Solutions
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
        myuser_info = myUser.objects.get(pk=user_id) 
        return render(request, 'index.html', {'user':myuser_info, 'user_authentication':True}) 
    return render(request, 'index.html',{'user_authentication':False})

def problemDetail(request, problem_detial_id):
    problem_detail_obj = get_object_or_404(Problem, pk = problem_detial_id)
    return render(request, 'problem_detail.html', {"problem_detail_key":problem_detail_obj})

def problemList(request):
    problem_list_item = Problem.objects.all()
    return render(request, 'problemList.html', {'problem_list_item':problem_list_item})

def solution(request):
    solution_item = Solution.objects.all()
    return render(request, 'solution.html', {'solution_item':solution_item})

def solutionDetail(request, solution_detail_id):
    solution_detail_item = get_object_or_404(Solution, pk = solution_detail_id)
    return render(request, 'solution_detail.html', {"solution_detail_item":solution_detail_item})

def writing(request):
    user_id = request.session.get('user')
    if request.method == "POST":
        filled_form = ProblemForm(request.POST)
        if filled_form.is_valid():
            post = filled_form.save(commit=False)
            post.userid = user_id
            post.save()
            return redirect('problemList') #problemList 중에서도 최신 순으로 나열되어 있는 페이지를 보여주는 게 좋을듯 (나중에 추가하자)
    prb_form = ProblemForm()
    return render(request, 'writing.html', {'prb_form':prb_form})

def signup(request):   #회원가입 기능
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        username = request.POST.get('username',None)  
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        res_data = {} 

        if (username):
            try:
                get_object_or_404(myUser,username=username)
                res_data['error'] = "이미 있는 아이디 입니다."
                return render(request, 'signup.html', res_data) 
            except :
                pass
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            user = myUser(username=username, password=make_password(password))
            user.save()
            return render(request,'index.html')
        return render(request, 'signup.html', res_data) 

def signin(request): #로그인 기능
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
            if check_password(login_password, myuser.password):
                request.session['user'] = myuser.id 
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/')
            else:
                response_data['error'] = "비밀번호가 틀렸습니다."

        return render(request, 'signin.html',response_data)

def signout(request): #로그아웃 기능
    logout(request) 
    return HttpResponseRedirect(reverse('index'))

def mypage(request):
    return render(request, 'mypage.html')

