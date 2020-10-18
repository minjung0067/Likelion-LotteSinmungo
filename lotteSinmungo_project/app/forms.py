
from .models import Problem,Solution,Photo
from django.contrib.auth.models import User
from django import forms

class ProblemForm(forms.ModelForm): # 만들어진 모델로부터 폼을 사용
    class Meta:
        model = Problem
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

class SolutionForm(forms.ModelForm): # 만들어진 모델로부터 폼을 사용
    class Meta:
        model = Solution
        fields = ('title','body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['maxlegth'] = 100
        self.fields['title'].label = "제목"
        self.fields['body'].label = "해결사항"

class PhotoUploadForm(forms.Form):
    """Image upload form.""" 
    image = forms.ImageField()