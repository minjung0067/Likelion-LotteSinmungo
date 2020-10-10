from django.shortcuts import render, redirect
from .forms import ProblemForm
from .models import Problem

# Create your views here.
def index(request):
    return render(request, 'index.html')

def problemList(request):
    return render(request, 'problemList.html')

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