from django.shortcuts import render,redirect
from .forms import PollForm,QuestionForm,AnswerForm
from .models import PollModel,QuestionModel,AnswerModel

def home(request):
	
	return render(request,"home.html")
	
	
def create(request):
	return render(request,"create.html")

def poll(request):
	data=PollModel.objects.all()
	return render(request,"poll.html",{"data":data})

def question(request):
	data=QuestionModel.objects.all()
	return render(request,"question.html",{"data":data})


def addpoll(request):
	if request.method=="POST":
		data=PollForm(request.POST)
		if data.is_valid():
			data.save()
			msg="poll created"
			print(data)
			fm1=PollForm()
			return render(request,"addpoll.html",{"fm1":fm1,"msg":msg})
	else:
		fm1=PollForm()
		return render(request,"addpoll.html",{"fm1":fm1})

def view(request,i):
	data=PollModel.objects.get(id=i)
	if request.method=="POST":
		op=request.POST.get("op")
		if op=="op1":
			data.op1c +=1
		elif op=="op2":
			data.op2c +=1
		else:
			data.op3c +=1

		data.save()
		return redirect("home")
	else:
		return render(request,"view.html",{"data":data})
def result(request,i):
	data=PollModel.objects.get(id=i)
	return render(request,"result.html",{"data":data})


def addquestion(request):
	if request.method=="POST":
		data=QuestionForm(request.POST)
		if data.is_valid():
			data.save()
			msg="Question created"
			print(data)
			fm2=QuestionForm()
			return render(request,"addquestion.html",{"fm2":fm2,"msg":msg})
	else:
		fm2=QuestionForm()
		return render(request,"addquestion.html",{"fm2":fm2})


def ans(request):
	data=QuestionModel.objects.get(qid=1)
	if request.method=="POST":
		data=AnswerForm(request.POST)
		if data.is_valid():
			data.save()
			msg="Question Answered"
			print(data)
			fm3=AnswerForm()
			return render(request,"ans.html",{"fm3":fm3,"msg":msg})
	else:
		fm3=AnswerForm()
		return render(request,"ans.html",{"fm3":fm3})


def viewans(request):
	data=AnswerModel.objects.get()
	print("DEBUG:", data)
	return render(request,"viewans.html",{"data":data})

