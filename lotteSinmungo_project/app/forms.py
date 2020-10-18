
from .models import Problem,Solution
from django.contrib.auth.models import User
from django import forms

class ProblemForm(forms.ModelForm): # 만들어진 모델로부터 폼을 사용
    class Meta:
        model = Problem
        fields = ('title','body','image')
        widgets = {
        'title': forms.TextInput(attrs={
            'class': 'form-title', 'style': 'height: auto; line-height: normal; width: 100%; padding: .8em .5em; margin: 3px; border: 0px; background-color: rgba(224, 224, 224, 0.493);;font-size: 16px;', 'placeholder': '불만사항을 한 줄로 요약해주세요 :D ♡',
            }),
        'body': forms.Textarea(attrs={
            'class': 'form-body', 'style': 'height: auto; line-height: normal; width: 100%; padding: .8em .5em; margin: 3px; border: 0px; background-color: rgba(224, 224, 224, 0.493);font-size: 16px;', 'placeholder': '불만사항을 자유롭게 적어주세요 :D ♡',
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['maxlegth'] = 100
        self.fields['title'].label = " "
        self.fields['body'].label = " "
        self.fields['image'].label = " "

class SolutionForm(forms.ModelForm): # 만들어진 모델로부터 폼을 사용
    class Meta:
        model = Solution
        fields = ('title','body','image')
        widgets = {
        'title': forms.TextInput(attrs={
            'class': 'form-title', 'style': 'width: 200%', 'placeholder': '제목을 입력해주세요.',
            }),
        'body': forms.Textarea(attrs={
            'class': 'form-body', 'style': 'width: 200%', 'placeholder': '내용을 입력해주세요.',
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['maxlegth'] = 100
        self.fields['title'].label = "제목"
        self.fields['body'].label = "불만사항"
        self.fields['image'].label = "이미지"

class PhotoUploadForm(forms.Form):
    """Image upload form.""" 
    image = forms.ImageField()