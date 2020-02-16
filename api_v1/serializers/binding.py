from rest_framework import serializers

from common.models import Binding
from ._base import BaseModelSerializer


class BindingSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Binding
