from .permissions import IsStuffOrReadOnly
from .models import Quiz
from .serializers import QuizSerializer
from rest_framework import viewsets


# Create your views here.
class QuizView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsStuffOrReadOnly,)
    

