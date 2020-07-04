from django.db.models import Q

from drf_writable_nested import WritableNestedModelSerializer

from rest_framework import serializers, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.pagination import LimitOffsetPagination

from api.models import DailyLiving
from users.models import User

from .other import OtherSerializer


class DailyLivingSerializer(WritableNestedModelSerializer):
    other = OtherSerializer(many=True, allow_null=True, required=False)
    users = PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all())

    class Meta:
        model = DailyLiving
        fields = "__all__"
        depth = 10


class DailyLivingViewSet(viewsets.ModelViewSet):
    serializer_class = DailyLivingSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        user = self.request.user
        qs = DailyLiving.objects.all()
        daily_living = qs.filter(users=user)
        return daily_living

