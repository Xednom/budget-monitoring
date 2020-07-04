from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.resources.insurance import InsuranceViewSet
from api.resources.income import IncomeViewSet
from api.resources.home_expense import HomeExpenseViewSet
from api.resources.daily_living import DailyLivingViewSet
from api.resources.saving import SavingViewSet
from api.resources.other import OtherViewSet


router = DefaultRouter()

router.register(r'income', IncomeViewSet, basename='Income')
router.register(r'insurance', InsuranceViewSet, basename='Insurance')
router.register(r'home-expense', HomeExpenseViewSet, basename='Home_expense')
router.register(r'daily-living', DailyLivingViewSet, basename='Daily_living')
router.register(r'saving', SavingViewSet, basename='Saving')
router.register(r'other', OtherViewSet)

urlpatterns = [
    path('', include(router.urls))
]