from django.urls import path
from rest_framework import routers

from quiz.views import QuizView

router = routers.DefaultRouter()
router.register('quiz',QuizView)

urlpatterns = [
  
] + router.urls
