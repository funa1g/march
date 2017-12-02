# coding: utf-8

from rest_framework import routers
from .views import CityViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'questions', QuestionViewSet, base_name='questions')
urlpatterns = router.urls
