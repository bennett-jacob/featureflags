from rest_framework import serializers

from common.models import Flag
from ._base import BaseModelSerializer


class FlagSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Flag
