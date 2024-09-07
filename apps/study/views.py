from django.shortcuts import render, get_object_or_404
from .models import Topic, Question, Answer
from rest_framework import viewsets
from .serializers import TopicSerializer, QuestionSerializer, AnswerSerializer
from .models import Test, TestResult, UserAnswer
from .serializers import TestSerializer, TestResultSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'study/topic_list.html', {'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    questions = topic.questions.all()
    return render(request, 'study/topic_detail.html', {'topic': topic, 'questions': questions})

def question_list(request, topic_id, difficulty):
    topic = get_object_or_404(Topic, pk=topic_id)
    questions = topic.questions.filter(difficulty=difficulty)

    return render(request, 'study/question_list.html', {'topic': topic, 'questions': questions, 'difficulty': difficulty})

class TopicViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class TestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    @action(detail=True, methods=['get'])
    def play(self, request, pk=None):
        test = self.get_object()
        questions = test.generate_questions()
        return Response(QuestionSerializer(questions, many=True).data)

    @action(detail=True, methods=['post'])
    def submit_answer(self, request, pk=None):
        test = self.get_object()
        question_id = request.data.get('question_id')
        answer_id = request.data.get('answer_id')
        
        question = Question.objects.get(id=question_id)
        answer = Answer.objects.get(id=answer_id)
               
        UserAnswer.objects.create(
            user=request.user,
            test=test,
            question=question,
            answer=answer
        )
        
        return Response({'status': 'answer recorded'})
    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        test = self.get_object()
        score = request.data.get('score')
        passed = score >= test.passing_score
        TestResult.objects.create(
            test=test,
            user=request.user,
            score=score,
            passed=passed
        )
        return Response({'passed': passed, 'score': score})
class TestResultViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
