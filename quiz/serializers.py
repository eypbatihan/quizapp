from rest_framework import serializers
from .models import Category,Quiz,Questions,Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("name","number_of_questions","time","required_score_to_pass","category","difficulty",)
