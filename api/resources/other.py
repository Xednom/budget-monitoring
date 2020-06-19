from django.db.models import Q

from drf_writable_nested import WritableNestedModelSerializer

from rest_framework import serializers, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from api.models import Other


class OtherSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Other
        fields = "__all__"
        depth = 10


class OtherViewSet(viewsets.ModelViewSet):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination