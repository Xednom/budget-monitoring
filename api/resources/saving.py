from django.db.models import Q

from drf_writable_nested import WritableNestedModelSerializer

from rest_framework import serializers, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.pagination import LimitOffsetPagination

from api.models import Saving
from users.models import User

from .other import OtherSerializer


class SavingSerializer(WritableNestedModelSerializer):
    other = OtherSerializer(many=True, allow_null=True, required=False)
    users = PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all())

    class Meta:
        model = Saving
        fields = "__all__"
        depth = 10


class SavingViewSet(viewsets.ModelViewSet):
    serializer_class = SavingSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        user = self.request.user
        qs = Saving.objects.all()
        saving = qs.filter(users=user)
        return saving

