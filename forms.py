from django import forms
from .models import PollModel,QuestionModel,AnswerModel

class PollForm(forms.ModelForm):
	class Meta:
		model=PollModel
		fields=["question","op1","op2","op3"]
		widgets={"question":forms.Textarea(attrs={"rows":4,"cols":22})}

class QuestionForm(forms.ModelForm):
	class Meta:
		model=QuestionModel
		fields=["qid","questions"]
		widgets={"questions":forms.Textarea(attrs={"rows":2,"cols":15})}

class AnswerForm(forms.ModelForm):
	class Meta:
		model=AnswerModel
		fields=["answer"]
		widgets={"answer":forms.Textarea(attrs={"rows":2,"cols":10})}

