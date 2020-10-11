
from django.shortcuts import render, redirect , get_object_or_404
from .forms import ProblemForm
from .models import Problem , myUser ,Solution
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.hashers import make_password, check_password 
from django.http import HttpResponse

from django.views.generic.list import ListView
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def index(request):

    return render(request, 'index.html')

def problemDetail(request, problem_detial_id):
    problem_detail_obj = get_object_or_404(Problem, pk = problem_detial_id)
    return render(request, 'problem_detail.html', {"problem_detail_key":problem_detail_obj})

def problemList(request):
    if request.GET.get('sort') == 'many_like':
        problem_list_item = Problem.objects.all().order_by('updated_at') #order_by를 통해 시간순(최근에서 내림차순) 정렬
    # elif request.GET.get('sort') == 'many_like':
    else:
        problem_list_item = Problem.objects.all().order_by('-title')
    return render(request, 'problemList.html', {'problem_list_item':problem_list_item})

# sort 구현 참고용
# def problemList(request):
#     sort = request.GET.get('sort', '')
#     if sort == 'many_like':
#         problem_list_item = Problem.objects.annotate(like_count = count('many_like')).order_by('-like_count', '-update_date')
#         return render(request, 'problemList.html', {'problem_list_item':problem_list_item})
#     elif sort == 'early_date':
#         problem_list_item = Problem.objects.order_by('-update_date')
#         return render(request, 'problemList.html', {'problem_list_item':problem_list_item})

def solution(request):
    solution_item = Solution.objects.all()
    return render(request, 'solution.html', {'solution_item':solution_item})

def solutionDetail(request, solution_detail_id):
    solution_detail_item = get_object_or_404(Solution, pk = solution_detail_id)
    return render(request, 'solution_detail.html', {"solution_detail_item":solution_detail_item})

def writing(request):
    user_id = request.user.id
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
            myuser = authenticate(request, username=login_username, password=login_password)
            if myuser is not None:
                login(request, myuser)
                return redirect('/')
            else:
                response_data['error'] = "비밀번호가 틀렸습니다."

        return render(request, 'signin.html',response_data)

def signout(request): #로그아웃 기능
    logout(request) 
    return HttpResponseRedirect(reverse('index'))

def mypage(request):
    return render(request, 'mypage.html')

@login_required
def problem_like(request, problem_detail_key_id):
    problem = get_object_or_404(Problem, id=problem_detail_key_id)
    user = request.user
    profile = myUser.objects.get(id=user.id)

    check_like_post = profile.like_problems.filter(id=problem_detail_key_id)

    if check_like_post.exists():
        profile.like_problems.remove(problem)
        problem.like_count -= 1
        problem.save()
    else:
        profile.like_problems.add(problem)
        problem.like_count += 1
        problem.save()

    return render(request, 'problem_detail.html', {"problem_detail_key":problem,"check_like_post" : check_like_post})