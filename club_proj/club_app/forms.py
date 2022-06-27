from django import forms
from .models import Club, Comment

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'number', 'introduction', 'logo']

    def __init__(self, *args, **kwargs):
        super(ClubForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : '동아리 이름을 입력하세요',
            'rows' : 30
        }

        self.fields['number'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : '인원수를 입력하세요',
            'rows' : 30
        }

        self.fields['introduction'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : '동아리 소개를 입력하세요',
            'rows' : 30,
            'cols' : 100
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : '댓글을 입력해주세요',
            'rows' : 10,
            'cols' : 100
        }