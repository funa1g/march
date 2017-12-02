import django_filters
from rest_framework import viewsets, filters

from .models import City, Question
from .serializer import CitySerializer, QuestionSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('id')


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('city_id', 'sort')

    def get_queryset(self):
        queryset = Question.objects.all()
        city_id = self.request.query_params.get('city_id', None)
        if city_id is not None:
            queryset = queryset.filter(city=city_id)
        return queryset
