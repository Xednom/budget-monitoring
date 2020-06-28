from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.resources.insurance import InsuranceViewSet
from api.resources.income import IncomeViewSet
from api.resources.other import OtherViewSet


router = DefaultRouter()

router.register(r'income', IncomeViewSet, basename='Income')
router.register(r'insurance', InsuranceViewSet, basename='Insurance')
router.register(r'other', OtherViewSet)

urlpatterns = [
    path('', include(router.urls))
]