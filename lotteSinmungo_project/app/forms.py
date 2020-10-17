
from .models import Problem,Solution
from django.contrib.auth.models import User
from django import forms

class ProblemForm(forms.ModelForm): # 만들어진 모델로부터 폼을 사용
    class Meta:
        model = Problem
        fields = ('title','body','image')
        widgets = {
        'title': forms.TextInput(attrs={
            'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.',
            })
        
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['maxlegth'] = 100
        self.fields['title'].label = "제목"
        self.fields['body'].label = "불만사항"

class SolutionForm(forms.ModelForm): # 만들어진 모델로부터 폼을 사용
    class Meta:
        model = Solution
        fields = ('title','body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['body'].label = "해결사항"

        
