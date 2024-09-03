from django.contrib import admin
from .models import Topic, Question, Answer, Test

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('text', 'topic', 'difficulty')
    list_filter = ('topic', 'difficulty')

admin.site.register(Topic)
admin.site.register(Question, QuestionAdmin)

class TestAdmin(admin.ModelAdmin):
    list_display = ('topic', 'number_of_questions', 'difficulty', 'passing_score', 'created_at')
    list_filter = ('topic', 'difficulty')
    search_fields = ('topic__name',)

admin.site.register(Test, TestAdmin)
