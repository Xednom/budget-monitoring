from django.db.models import Q

from drf_writable_nested import WritableNestedModelSerializer

from rest_framework import serializers, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.pagination import LimitOffsetPagination

from api.models import Income
from users.models import User

from .other import OtherSerializer


class IncomeSerializer(WritableNestedModelSerializer):
    other = OtherSerializer(many=True, allow_null=True)
    users = PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all())

    class Meta:
        model = Income
        fields = "__all__"
        depth = 10


class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        user = self.request.user
        qs = Income.objects.all()
        income = qs.filter(users=user)
        return income

