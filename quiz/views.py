from rest_framework import generics
from quiz.models import Question, Quizzes
from quiz.serializer import QuestionSerializer, QuizSerializer, RandomQuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Quiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer


class RandomQuestion(APIView):
    def get(self, request, formt=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs["topic"]).order_by("?")[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    def get(self, request, formt=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs["topic"])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)
