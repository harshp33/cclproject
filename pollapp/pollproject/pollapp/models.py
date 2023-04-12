from django.db import models

class PollModel(models.Model):
	question=models.TextField()
	op1=models.CharField(max_length=30)
	op2=models.CharField(max_length=30)
	op3=models.CharField(max_length=30)
	op1c=models.IntegerField(default=0)
	op2c=models.IntegerField(default=0)
	op3c=models.IntegerField(default=0)

class QuestionModel(models.Model):
	qid=models.IntegerField()
	questions=models.TextField()

class AnswerModel(models.Model):
	answer=models.TextField()
	
def __str__(self):
	return self.question
	return self.questions
	return self.answer