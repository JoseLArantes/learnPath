from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'study'

router = DefaultRouter()
router.register(r'topics', views.TopicViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'tests', views.TestViewSet)
router.register(r'test-results', views.TestResultViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.topic_list, name='topic_list'),
    path('<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('<int:topic_id>/<str:difficulty>/', views.question_list, name='question_list'),
    path('app/', views.StudyAppView.as_view(), name='study_app'),
]