from django import forms
fromm .models import Comment
class CommentForm(forms.ModelForm):
		class Meta:
			model = Comment
			fields = ('user','email','body')