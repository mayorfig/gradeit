from django.db import models

# Create your models here.
class Question(models.Model):
    """ A model of the 8 questions. """
    question_title = models.TextField(max_length=100000)
    set = models.IntegerField(unique=True)
    min_score = models.IntegerField()
    max_score = models.IntegerField()

    def __str__(self):
        return str(self.set)

class Essay(models.Model):
    """ Essay to be submitted. """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(max_length=100000)
    score = models.IntegerField(null=True, blank=True)
    matric_no = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
