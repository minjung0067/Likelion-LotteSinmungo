from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProblemForm, SigninForm, SignupForm#이전에 만든 form 클래스를 선언해주고
from .models import Problem
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import User

from django.views.generic.list import ListView



def index(request):
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

def signup(request):#역시 GET/POST 방식을 사용하여 구현한다.
    if request.method == "GET":
        return render(request, 'signup.html', {'f':SignupForm()} )
    
    
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password']  == form.cleaned_data['password_check']:
#cleaned_data는 사용자가 입력한 데이터를 뜻한다.
#즉 사용자가 입력한 password와 password_check가 맞는지 확인하기위해 작성해주었다.

                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
#User.object.create_user는 사용자가 입력한 name, email, password를 가지고 아이디를 만든다.
#바로 .save를 안해주는 이유는 User.object.create를 먼저 해주어야 비밀번호가 암호화되어 저장된다.

                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
#나머지 입력하지 못한 last_name과, first_name은 따로 지정해준다.
                new_user.save()
                
                return HttpResponseRedirect(reverse('vote:index'))      
            else:
                return render(request, 'signup.html',{'f':form, 'error':'비밀번호와 비밀번호 확인이 다릅니다.'})#password와 password_check가 다를 것을 대비하여 error를 지정해준다.

        else: #form.is_valid()가 아닐 경우, 즉 유효한 값이 들어오지 않았을 경우는

            return render(request, 'signup.html',{'f':form})

