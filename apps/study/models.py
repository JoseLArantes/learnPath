from django.db import models
from django.contrib.auth.models import User
import random

class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions', default=1)
    text = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')

    def __str__(self):
        return f"{self.topic.name} - {self.text[:50]}..."

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Test(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    number_of_questions = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=10, choices=Question.DIFFICULTY_CHOICES)
    passing_score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_questions(self):
        questions = Question.objects.filter(topic=self.topic, difficulty=self.difficulty)
        return random.sample(list(questions), min(self.number_of_questions, questions.count()))

class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    passed = models.BooleanField()
    completed_at = models.DateTimeField(auto_now_add=True)

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
